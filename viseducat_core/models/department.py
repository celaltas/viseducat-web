from odoo import models, fields, api


class VmDepartment(models.Model):
    _name = "vm.department"
    _description = "Department"

    name = fields.Char('Name')
    code = fields.Char('Code')
    parent_id = fields.Many2one('vm.department', 'Parent Department')

    @api.model
    def create(self, vals):
        department = super(VmDepartment, self).create(vals)
        self.env.user.write({'department_ids': [(4, department.id)]})
        return department
