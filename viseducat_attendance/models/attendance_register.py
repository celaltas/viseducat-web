from odoo import models, fields, api


class VmAttendanceRegister(models.Model):
    _name = "vm.attendance.register"
    _inherit = ["mail.thread"]
    _description = "Attendance Register"
    _order = "id DESC"

    name = fields.Char(
        'Name', size=16, required=True, track_visibility='onchange')
    code = fields.Char(
        'Code', size=16, required=True, track_visibility='onchange')
    course_id = fields.Many2one(
        'vm.course', 'Course', required=True, track_visibility='onchange')
    batch_id = fields.Many2one(
        'vm.batch', 'Batch', required=True, track_visibility='onchange')
    subject_id = fields.Many2one(
        'vm.subject', 'Subject', track_visibility='onchange')
    active = fields.Boolean(default=True)

    attendance_onboarding_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done"), ('closed', "Closed")],
        string="State of the attendances onboarding panel", default='not_done')
    attendance_onboarding_register_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the onboarding register layout step", default='not_done')
    attendance_onboarding_sheet_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the sheet onboarding panel", default='not_done')
    attendance_onboarding_lines_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the lines onboarding panel", default='not_done')

    _sql_constraints = [
        ('unique_attendance_register_code',
         'unique(code)', 'Code should be unique per attendance register!')]

    @api.depends('course_id')
    def onchange_course(self):
        if not self.course_id:
            self.batch_id = False

    # Onboarding Methods
    @api.model
    def action_open_attendance_register_onboarding(self):
        action=self.env.ref('viseducat_attendance.action_open_attendance_onboarding_register_step').read()[0]
        return action

    @api.model
    def action_open_attendance_sheet_onboarding(self):
        action = self.env.ref('viseducat_attendance.action_open_attendance_onboarding_sheet_step').read()[0]
        return action

    @api.model
    def action_open_attendance_lines_onboarding(self):
        action = self.env.ref('viseducat_attendance.action_open_attendance_onboarding_lines_step').read()[0]
        return action

    def get_and_update_atendance_dashboard_onboarding_state(self):
        steps = [
            'attendance_onboarding_register_layout_state',
            'attendance_onboarding_sheet_layout_state',
            'attendance_onboarding_lines_layout_state',
        ]
        return self.get_and_update_onbarding_state('attendance_onboarding_state', steps)

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

    def action_save_onboarding_register_step(self):
        self.set_onboarding_step_done('attendance_onboarding_register_layout_state')

    @api.model
    def action_close_attendance_onboarding(self):
        attendance =self.env['vm.attendance.register'].search([], limit=1, order="id desc")
        attendance.attendance_onboarding_state = "closed"
