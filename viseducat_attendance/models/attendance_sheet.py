from odoo import models, fields, api


class VmAttendanceSheet(models.Model):
    _name = "vm.attendance.sheet"
    _inherit = ["mail.thread"]
    _description = "Attendance Sheet"
    _order = "attendance_date desc"

    name = fields.Char('Name', readonly=True, size=32)
    register_id = fields.Many2one(
        'vm.attendance.register', 'Register', required=True,
        track_visibility="onchange")
    course_id = fields.Many2one(
        'vm.course', related='register_id.course_id', store=True,
        readonly=True)
    batch_id = fields.Many2one(
        'vm.batch', 'Batch', related='register_id.batch_id', store=True,
        readonly=True)
    session_id = fields.Many2one('vm.session', 'Session')
    attendance_date = fields.Date(
        'Date', required=True, default=lambda self: fields.Date.today(),
        track_visibility="onchange")
    attendance_line = fields.One2many(
        'vm.attendance.line', 'attendance_id', 'Attendance Line')
    total_present = fields.Integer(
        'Total Present', compute='_compute_total_present',
        track_visibility="onchange")
    total_absent = fields.Integer(
        'Total Absent', compute='_compute_total_absent',
        track_visibility="onchange")
    faculty_id = fields.Many2one('vm.faculty', 'Faculty')
    active = fields.Boolean(default=True)

    state = fields.Selection(
        [('draft', 'Draft'), ('start', 'Attendance Start'),
         ('done', 'Attendance Taken'), ('cancel', 'Cancelled')],
        'Status', default='draft', track_visibility='onchange')

    _sql_constraints = [
        ('unique_register_sheet',
         'unique(register_id,session_id,attendance_date)',
         'Sheet must be unique per Register/Session.'),
    ]


    def action_save_onboarding_sheet_step(self):
        attendance=self.env['vm.attendance.register'].search([],limit=1,order='id desc')
        attendance.sudo().set_onboarding_step_done('attendance_onboarding_sheet_layout_state')

    @api.model
    def create(self, vals):
        sheet = self.env['ir.sequence'].next_by_code('vm.attendance.sheet')
        register = self.env['vm.attendance.register']. \
            browse(vals['register_id']).code
        vals['name'] = register + sheet
        return super(VmAttendanceSheet, self).create(vals)

    @api.depends('attendance_line.present')
    def _compute_total_present(self):
        for record in self:
            record.total_present = self.env['vm.attendance.line'].search_count(
                [('present', '=', True), ('attendance_id', '=', record.id)])

    @api.depends('attendance_line.present')
    def _compute_total_absent(self):
        for record in self:
            record.total_absent = self.env['vm.attendance.line'].search_count(
                [('present', '=', False), ('attendance_id', '=', record.id)])

    def attendance_draft(self):
        self.state = 'draft'

    def attendance_start(self):
        self.state = 'start'

    def attendance_done(self):
        self.state = 'done'

    def attendance_cancel(self):
        self.state = 'cancel'