from odoo import models, fields, api, _


class VmSubject(models.Model):
    _name = "vm.subject"
    _inherit = "mail.thread"
    _description = "Subject"

    name = fields.Char('Name', size=128, required=True)
    code = fields.Char('Code', size=256, required=True)
    grade_weightage = fields.Float('Grade Weightage')
    type = fields.Selection(
        [('theory', 'Theory'), ('practical', 'Practical'),
         ('both', 'Both'), ('other', 'Other')],
        'Type', default="theory", required=True)
    subject_type = fields.Selection(
        [('compulsory', 'Compulsory'), ('elective', 'Elective')],
        'Subject Type', default="compulsory", required=True)
    department_id = fields.Many2one(
        'vm.department', 'Department',
        default=lambda self:
        self.env.user.dept_id and self.env.user.dept_id.id or False)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_subject_code',
         'unique(code)', 'Code should be unique per subject!'),
    ]


    def action_save_onboarding_subject_step(self):
        course = self.env['vm.course'].search([], limit=1, order="id desc")
        course.sudo().set_onboarding_step_done('course_onboarding_subject_layout_state')

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Subjects'),
            'template': '/viseducat_core/static/xls/vm_subject.xls'
        }]
