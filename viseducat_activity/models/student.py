from odoo import models, fields


class VmStudent(models.Model):
    _inherit = "vm.student"

    activity_log = fields.One2many('vm.activity', 'student_id',
                                   string='Activity Log')
    activity_count = fields.Integer(compute='compute_count')

    def get_activity(self):
        action = self.env.ref('viseducat_activity.act_open_vm_activity_view').read()[0]
        action['domain'] = [('student_id', 'in', self.ids)]
        return action


    def compute_count(self):
        for record in self:
            record.activity_count = self.env['vm.activity'].search_count([('student_id', 'in', self.ids)])
