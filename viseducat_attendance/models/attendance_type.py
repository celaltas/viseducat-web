from odoo import models, fields


class VmAttendanceType(models.Model):
    _name = "vm.attendance.type"
    _inherit = ["mail.thread"]
    _description = "Attendance Type"

    name = fields.Char(
        'Name', size=20, required=True, track_visibility='onchange')
    active = fields.Boolean(default=True)
    present = fields.Boolean(
        'Present ?', track_visibility="onchange")
    excused = fields.Boolean(
        'Excused ?', track_visibility="onchange")
