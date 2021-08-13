from odoo import models, fields


class WizardOpFacultyEmployee(models.TransientModel):
    _name = 'wizard.vm.faculty.employee'
    _description = "Create Employee and User of Faculty"

    user_boolean = fields.Boolean("Want to create user too ?", default=True)

    def create_employee(self):
        for record in self:
            active_id = self.env.context.get('active_ids', []) or []
            faculty = self.env['vm.faculty'].browse(active_id)
            faculty.create_employee()
            if record.user_boolean and not faculty.user_id:
                user_group = self.env.ref('viseducat_core.group_vm_faculty')
                self.env['res.users'].create_user(faculty, user_group)
                faculty.emp_id.user_id = faculty.user_id