from odoo import models, fields


class VmCourseEnrollmentMaterial(models.Model):
    _name = "vm.course.enrollment.material"
    _description = "Course Enrollment Material"

    enrollment_id = fields.Many2one('vm.course.enrollment', 'Enrollment')
    material_id = fields.Many2one('vm.material', 'Material', required=True)
    completed = fields.Boolean('Completed')
    completed_date = fields.Datetime('Completed Date')
    last_access_date = fields.Datetime('Last Access Date')


class VmCourseEnrollment(models.Model):
    _name = "vm.course.enrollment"
    _description = "Course Enrollments"
    _rec_name = "index"

    index = fields.Char('Index')
    course_id = fields.Many2one("vm.course", string="Course", required=True)
    user_id = fields.Many2one("res.users", string="User", required=True)
    order_id = fields.Many2one("sale.order", string="Order", required=True)
    completion_date = fields.Datetime('Completion Date', required=True, )
    enrollment_date = fields.Datetime('Enrollment Date', required=True, default=fields.Datetime.today())
    state = fields.Selection(
        [('draft', 'Draft'),
         ('in_progress', 'In Progress'), ('done', 'Done')],
        'State', default='draft')

    navigation_policy = fields.Selection([
        ('free_learn', 'Free Learning Path'), ('seq_learn', 'Sequential Learning Path')], 'Navigation Policy')

    completed_percentage = fields.Integer('Completed Percentage', default=0)
    enrollment_material_line = fields.One2many('vm.course.enrollment.material', 'enrollment_id',
                                               'Materials',
                                               track_visibility='onchange')

    active = fields.Boolean(default=True)

    def action_onboarding_enrollment_layout(self):
        course = self.env['vm.course'].search([('online_course', '=', True)], limit=1, order="id desc")
        course.sudo().set_onboarding_step_done('course_onboarding_lms_enrollment_layout_state')


