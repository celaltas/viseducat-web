from odoo import models, fields
from datetime import datetime


class VmBatchInherit(models.Model):
    _inherit = "vm.batch"

    today_lecture = fields.Integer(compute='today_lecture_compute', string="Today's Lecture")

    def today_lecture_compute(self):
        for record in self:
            today = datetime.today().strftime("%A")
            record.today_lecture = self.env['vm.session'].search_count(
                [('type', '=', today),('course_id.id','=',record.id)])

    def action_open_vm_session_view(self):
        action = self.env.ref('viseducat_timetable.act_open_vm_session_view').read()[0]
        today = datetime.today().strftime("%A")
        action['domain'] = [('type', '=', today)]

        return action
