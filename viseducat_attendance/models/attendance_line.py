from odoo import models, fields, api


class VmAttendanceLine(models.Model):
    _name = "vm.attendance.line"
    _inherit = ["mail.thread"]
    _rec_name = "attendance_id"
    _description = "Attendance Lines"
    _order = "attendance_date desc"

    attendance_id = fields.Many2one(
        'vm.attendance.sheet', 'Attendance Sheet', required=True,
        track_visibility="onchange", ondelete="cascade")
    student_id = fields.Many2one(
        'vm.student', 'Student', required=True, track_visibility="onchange")
    present = fields.Boolean(
        'Present ?', default=True, track_visibility="onchange")
    excused = fields.Boolean(
        'Excused ?', track_visibility="onchange")
    course_id = fields.Many2one(
        'vm.course', 'Course',
        related='attendance_id.register_id.course_id', store=True,
        readonly=True)
    batch_id = fields.Many2one(
        'vm.batch', 'Batch',
        related='attendance_id.register_id.batch_id', store=True,
        readonly=True)
    remark = fields.Char('Remark', size=256, track_visibility="onchange")
    attendance_date = fields.Date(
        'Date', related='attendance_id.attendance_date', store=True,
        readonly=True, track_visibility="onchange")
    register_id = fields.Many2one(
        related='attendance_id.register_id', store=True)
    active = fields.Boolean(default=True)
    attendance_type_id = fields.Many2one(
        'vm.attendance.type', 'Attendance Type',
        required=False, track_visibility='onchange')

    _sql_constraints = [
        ('unique_student',
         'unique(student_id,attendance_id,attendance_date)',
         'Student must be unique per Attendance.'),
    ]

    def action_save_onboarding_line_step(self):
        attendance = self.env['vm.attendance.register'].search([], limit=1, order='id desc')
        attendance.sudo().set_onboarding_step_done('attendance_onboarding_lines_layout_state')

    @api.onchange('attendance_type_id')
    def onchange_attendance_type(self):
        if self.attendance_type_id:
            self.present = self.attendance_type_id.present
            self.excused = self.attendance_type_id.excused
