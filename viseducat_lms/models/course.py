from odoo import models, fields, api, _
from datetime import date


class VmCourseInherit(models.Model):
    _inherit = 'vm.course'

    online_course = fields.Boolean('Online Course?', default=True, readonly=True)
    image_1920 = fields.Image('Course Image')
    confirm_date = fields.Date('Confirm Date', )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('open', 'Confirm'), ('closed', 'Closed')],
        'State', default='draft', track_visibility='onchange')
    section_count = fields.Integer(compute='section_count_compute')
    training_material = fields.Integer(compute='training_material_count_compute')
    course_completed = fields.Integer(compute='course_completed_compute')
    enrolled_users = fields.Integer(compute='enrolled_users_compute')

    user_id = fields.Many2one("res.users", string="User", readonly=True, required=True,
                              default=lambda self: self.env.user.id)

    # forum_id = fields.Many2one('blog.blog', 'Blog', readonly=True)

    visibility = fields.Selection([
        ('public', 'Everyone'), ('logged_user', 'Only logged in User'), ('invited_user', 'Only Invited User')
    ], 'Visibility Policy')
    course_attempt_reward = fields.Integer('Attempt Reward', default=0)
    certificate = fields.Boolean('Certificate')
    title = fields.Boolean('Title')
    certi_title = fields.Char('Certificate Title')
    certi_date = fields.Boolean('Certificate Date')
    certi_num = fields.Boolean('Certificate Number')
    background = fields.Image('Background Image')
    type = fields.Selection([
        ('free', 'Free'), ('paid', 'Paid')], 'Type')
    navigation_policy = fields.Selection([
        ('free_learn', 'Free Learning Path'), ('seq_learn', 'Sequential Learning Path')], 'Navigation Policy')
    short_description = fields.Char('Short Description', size=80)
    full_description = fields.Html('Full Description')
    course_section_ids = fields.One2many('vm.course.section', 'course_id',
                                         'Course Section',
                                         track_visibility='onchange')
    total_time = fields.Float("Total Time(HH:MM)", required=True, default=0.0)
    faculty_ids = fields.Many2many('vm.faculty')
    suggested_course_ids = fields.Many2many('vm.course', 'vm_course_rel', 'name', 'code', 'evaluation_type', )
    category_ids = fields.Many2many('vm.course.category', string='Categories')
    invited_users_ids = fields.Many2many('res.users', string='Invited Users')

    course_to_begin = fields.Integer('Course to Begin', default=0, compute='course_to_begin_compute')
    days_since_launch = fields.Integer('Days Since Launch', default=0, compute='days_since_launch_compute')
    course_in_progress = fields.Integer(' Course In Progress', default=0)
    display_time = fields.Float('Duration', default=0, compute='display_time_compute')

    # courses onboarding panel
    lms_courses_onboarding_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done"), ('closed', "Closed")],
        string="State of the lms courses onboarding panel", default='not_done')
    course_onboarding_lms_course_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the lms onboarding course layout step", default='not_done')
    course_onboarding_lms_material_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the lms onboarding material layout step", default='not_done')
    course_onboarding_lms_enrollment_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the lms onboarding enrollment layout step", default='not_done')
    course_onboarding_lms_category_layout_state = fields.Selection(
        [('not_done', "Not done"), ('just_done', "Just done"), ('done', "Done")],
        string="State of the lms onboarding course category layout step", default='not_done')


    def section_count_compute(self):
        for record in self:
            record.section_count = len(self.course_section_ids)

    def training_material_count_compute(self):
        for record in self:
            material_of_section = [len(section.section_material_ids) for section in record.course_section_ids]
            record.training_material = sum(material_of_section)

    def course_completed_compute(self):
        for record in self:
            record.course_completed = 1

    def enrolled_users_compute(self):
        # State draft değiştirmen lazım
        for record in self:
            record.enrolled_users = self.env['vm.course.enrollment'].search_count(
                [('state', '=', 'draft'), ('course_id', '=', record.id)])

    def action_view_section(self):
        action = self.env.ref('viseducat_lms.act_open_vm_course_section_view').read()[0]
        action['context'] = {'default_course_id': self.id}
        action['domain'] = [('course_id', '=', self.id)]
        return action

    def action_view_material(self):
        material_ids = []
        for section in self.course_section_ids:
            for record in section.section_material_ids:
                material_ids.append(record.material_id.id)
        action = self.env.ref('viseducat_lms.act_open_vm_material_view').read()[0]
        action['domain'] = [('id', 'in', material_ids)]
        return action

    def action_view_users(self):
        print("calculate user method")

    def action_course_completed(self):
        print("see course completed users")

    def days_since_launch_compute(self):
        for record in self:
            if record.confirm_date:
                first_date = record.confirm_date
                last_date = date.today()
                record.days_since_launch = (last_date - first_date).days
            record.days_since_launch = 0

    def display_time_compute(self):

        for record in self:
            total = 0
            for rec in record.course_section_ids:
                total += rec.total_time
            record.display_time = total

    def course_to_begin_compute(self):
        # tekrar bak
        self.course_to_begin = 0

    def action_draft(self):
        self.confirm_date = False
        self.state = 'draft'

    def action_confirm(self):
        self.confirm_date = date.today()
        self.state = 'open'

    def action_closed(self):
        if self.blog_id is True:
            print("blog id var")

        else:
            print("blog id yok")

        self.state = 'closed'

    # lms courses onboarding panel methods
    @api.model
    def action_open_lms_course_layout_onboarding(self):
        action = self.env.ref('viseducat_lms.action_open_lms_onboarding_course_layout_step').read()[0]
        return action

    @api.model
    def action_open_lms_material_layout_onboarding(self):
        action = self.env.ref('viseducat_lms.action_open_lms_onboarding_material_layout_step').read()[0]
        return action

    @api.model
    def action_open_lms_enrollment_layout_onboarding(self):
        action = self.env.ref('viseducat_lms.action_open_lms_onboarding_enrollment_layout_step').read()[0]
        return action

    @api.model
    def action_open_lms_course_category_layout_onboarding(self):
        action = self.env.ref('viseducat_lms.action_open_lms_onboarding_course_category_layout_step').read()[0]
        return action

    def action_lms_onboarding_course_layout(self):
        self.set_onboarding_step_done('course_onboarding_lms_course_layout_state')

    def get_and_update_lms_course_dashboard_onboarding_state(self):

        steps = [
            'course_onboarding_lms_course_layout_state',
            'course_onboarding_lms_material_layout_state',
            'course_onboarding_lms_enrollment_layout_state',
            'course_onboarding_lms_category_layout_state',
        ]
        return self.get_and_update_onbarding_state('lms_courses_onboarding_state', steps)

    @api.model
    def action_close_lms_course_onboarding(self):
        course = self.env['vm.course'].search([('online_course', '=', True)], limit=1, order="id desc")
        course.lms_courses_onboarding_state = "closed"
