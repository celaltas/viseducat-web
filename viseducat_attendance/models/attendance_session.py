from odoo import models, fields


class VmSession(models.Model):
    _inherit = "vm.session"

    attendance_sheet = fields.One2many('vm.attendance.sheet', 'session_id', string='Session')

    def get_attendance(self):
        sheet = self.env['vm.attendance.sheet'].search([('session_id', '=', self.id)])
        register = register = self.env['vm.attendance.register'].search(
            [('course_id', '=', self.course_id.id), ('batch_id', '=', self.batch_id.id)])

        if self.id == sheet.session_id.id:
            if len(sheet) <= 1:
                view_id = self.env.ref('viseducat_attendance.view_vm_attendance_sheet_form').id
                return {
                    'name': 'Attendance Sheet',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'views': [(view_id, 'form')],
                    'type': 'ir.actions.act_window',
                    'res_model': 'vm.attendance.sheet',
                    'res_id': sheet.id,
                    'target': 'current',
                    'context': {'default_session_id': self.id,
                                'default_register_id': [rec.id for rec in register]},
                    'domain': [('session_id', "=", sheet.session_id.id)]

                }
            action = self.env.ref('viseducat_attendance.act_vis_vm_attendance_sheet_view').read()[0]
            action['context'] = {
                'default_session_id': self.id,
                'default_register_id': [rec.id for rec in register]}
            action['domain'] = [('session_id', '=', self.id)]

            return action

        else:

            view_id = self.env.ref('viseducat_attendance.view_vm_attendance_sheet_form').id
            return {
                'name': 'Attendance Sheet',
                'view_type': 'form',
                'view_mode': 'tree',
                'views': [(view_id, 'form')],
                'res_model': 'vm.attendance.sheet',
                'view_id': False,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'context': {'default_session_id': self.id,
                            'default_register_id': [rec.id for rec in register]},
                'domain': [('session_id', "=", self.id)]
            }
