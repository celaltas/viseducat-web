from odoo import models, fields


class VmStudent(models.Model):
    _inherit = "vm.student"

    allocation_ids = fields.Many2many('vm.assignment', string='Assignment(s)')
    assignment_count = fields.Integer(compute='compute_count_assignment')

    def get_assignment(self):
        action = self.env.ref('viseducat_assignment.act_open_vm_assignment_view').read()[0]
        action['domain'] = [('allocation_ids', 'in', self.ids)]
        return action

    def compute_count_assignment(self):
        for record in self:
            record.assignment_count = self.env['vm.assignment'].search_count([('allocation_ids', '=', self.id)])
