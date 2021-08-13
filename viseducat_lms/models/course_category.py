from odoo import models, fields


class VmCourseCategory(models.Model):
    _name = "vm.course.category"
    _description = "Course Category"


    name = fields.Char('Name', size=32, required=True)
    code = fields.Char('Code', required=True)
    icon = fields.Char('Icon')
    description = fields.Text("Description")



    _sql_constraints = [
        ('unique_course_category_code',
         'unique(code)', 'Code should be unique per course category!')]




    def action_onboarding_course_category_layout(self):
        course = self.env['vm.course'].search([('online_course', '=', True)], limit=1, order="id desc")
        course.sudo().set_onboarding_step_done('course_onboarding_lms_category_layout_state')
