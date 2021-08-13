from odoo import models, fields, api, _


class VmCourse(models.Model):
    _name = "vm.course"
    _inherit = "mail.thread"
    _description = "Course"

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', size=16, required=True)
    parent_id = fields.Many2one('vm.course', 'Parent Course')
    evaluation_type = fields.Selection(
        [('normal', 'Normal'), ('GPA', 'GPA'),
         ('CWA', 'CWA'), ('CCE', 'CCE')],
        'Evaluation Type', default="normal", required=True)
    subject_ids = fields.Many2many('vm.subject', string='Subject(s)')
    max_unit_load = fields.Float("Maximum Unit Load")
    min_unit_load = fields.Float("Minimum Unit Load")
    department_id = fields.Many2one(
        'vm.department', 'Department',
        default=lambda self:
        self.env.user.dept_id and self.env.user.dept_id.id or False)
    active = fields.Boolean(default=True)
    student_count = fields.Integer(compute='student_count_compute', string='Number of Student')
    child_course_count = fields.Integer(compute='child_course_count_compute', string='Number of Child Course')
    subject_count = fields.Integer(compute='subject_count_compute', string='Number of Subject')
    batch_count = fields.Integer(compute='batch_count_compute', string='Number of Batch')
    admission_count = fields.Integer(compute='admission_count_compute', string='Number of Admission')
    timetable_count = fields.Integer(compute='timetable_count_compute', string='Number of Timetable')
    color = fields.Integer("Color Index", default=0)

    # courses onboarding panel
    courses_onboarding_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done"), ('closed', "Closed")],
        string="State of the courses onboarding panel", default='not_done')
    course_onboarding_course_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the onboarding course layout step", default='not_done')
    course_onboarding_batch_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the batch onboarding panel", default='not_done')
    course_onboarding_subject_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the subject onboarding panel", default='not_done')

    _sql_constraints = [
        ('unique_course_code',
         'unique(code)', 'Code should be unique per course!')]

    # course dashboard methods

    def student_count_compute(self):
        for record in self:
            record.student_count = self.env['vm.student'].search_count(
                [('course_detail_ids.course_id', '=', record.id)])

    def action_open_vm_student_view(self):
        action = self.env.ref('viseducat_core.act_open_vm_student_view_2').read()[0]
        action['domain'] = [('course_detail_ids.course_id', '=', self.id)]
        return action

    def child_course_count_compute(self):
        for record in self:
            record.child_course_count = self.search_count(
                [('parent_id', '=', record.id)])

    def action_open_vm_child_course_view(self):
        action = self.env.ref('viseducat_core.act_open_vm_course_dashboard').read()[0]
        action['domain'] = [('parent_id', '=', self.id)]
        return action

    def subject_count_compute(self):
        for record in self:
            courses = self.search([('id', '=', record.id)])
            for course in courses:
                record.subject_count = len(course.subject_ids)

    def admission_count_compute(self):
        for record in self:
            record.admission_count = self.env['vm.admission'].search_count(
                [('course_id', '=', record.id)])

    def timetable_count_compute(self):
        for record in self:
            record.timetable_count = self.env['vm.session'].search_count(
                [('course_id', '=', record.id)])

    def action_open_vm_subject_view(self):
        action = self.env.ref('viseducat_core.act_open_vm_subject_view').read()[0]
        subject_in_course = self.search([('id', '=', self.id)]).subject_ids.ids
        action['domain'] = [('id', 'in', subject_in_course)]
        return action

    def batch_count_compute(self):
        for record in self:
            record.batch_count = self.env['vm.batch'].search_count([('course_id', '=', record.id)])

    def action_open_vm_batch_view(self):
        action = self.env.ref('viseducat_core.act_open_vm_batch_view').read()[0]
        action['domain'] = [('course_id', '=', self.id)]
        return action

    def action_open_vm_admissiom_view(self):
        action = self.env.ref('viseducat_admission.act_open_vm_admission_view').read()[0]
        action['domain'] = [('course_id', '=', self.id)]
        return  action

    def action_open_vm_timetable_view(self):
        action = self.env.ref('viseducat_timetable.act_open_vm_session_view').read()[0]
        action['domain'] = [('course_id', '=', self.id)]
        return action




    # courses onboarding panel methods
    @api.model
    def action_open_course_onboarding(self):
        action = self.env.ref('viseducat_core.action_open_course_onboarding_course_step').read()[0]
        return action

    @api.model
    def action_open_batch_onboarding(self):
        action = self.env.ref('viseducat_core.action_open_course_onboarding_batch_step').read()[0]
        return action

    @api.model
    def action_open_subject_onboarding(self):
        action = self.env.ref('viseducat_core.action_open_course_onboarding_subject_step').read()[0]
        return action

    def get_and_update_course_dashboard_onboarding_state(self):
        steps = [
            'course_onboarding_course_layout_state',
            'course_onboarding_batch_layout_state',
            'course_onboarding_subject_layout_state',
        ]
        return self.get_and_update_onbarding_state('courses_onboarding_state', steps)

    def set_onboarding_step_done(self, step_name):
        if self[step_name] == 'not_done':
            self[step_name] = 'just_done'


    def get_and_update_onbarding_state(self, onboarding_state, steps_states):
        old_values = {}
        all_done = True
        for step_state in steps_states:
            old_values[step_state] = self[step_state]
            if self[step_state] == 'just_done':
                self[step_state] = 'done'
            all_done = all_done and self[step_state] == 'done'
        if all_done:
            if self[onboarding_state] == 'not_done':
                old_values['onboarding_state'] = 'just_done'
            else:
                old_values['onboarding_state'] = 'done'
            self[onboarding_state] = 'done'
        return old_values

    def action_save_onboarding_course_step(self):
        self.set_onboarding_step_done('course_onboarding_course_layout_state')

    @api.model
    def action_close_course_onboarding(self):
        course = self.env['vm.course'].search([], limit=1, order="id desc")
        course.courses_onboarding_state = "closed"


    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Courses'),
            'template': '/viseducat_core/static/xls/vm_course.xls'
        }]
