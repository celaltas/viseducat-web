from odoo import models, fields
from datetime import date



class VmBatchInherit(models.Model):
    _inherit = "vm.batch"

    total_present = fields.Integer(
        'Total Present', compute='_compute_total_present', track_visibility="onchange")
    total_absent = fields.Integer(
        'Total Absent', compute='_compute_total_absent', track_visibility="onchange")



    def _compute_total_present(self):
        for record in self:
            record.total_present = self.env['vm.attendance.line'].search_count(
                [('present', '=', True), ('batch_id', '=', record.id), ('attendance_date', '=',date.today())])


    def _compute_total_absent(self):
        for record in self:
            record.total_absent = self.env['vm.attendance.line'].search_count(
                [('present', '=', False), ('batch_id', '=', record.id), ('attendance_date', '=', date.today())])
