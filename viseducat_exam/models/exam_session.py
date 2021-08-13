
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VmExamSession(models.Model):
    _name = "vm.exam.session"
    _inherit = ["mail.thread"]
    _description = "Exam Session"

    name = fields.Char(
        'Exam Session', size=256, required=True, track_visibility='onchange')
    course_id = fields.Many2one(
        'vm.course', 'Course', required=True, track_visibility='onchange')
    batch_id = fields.Many2one(
        'vm.batch', 'Batch', required=True, track_visibility='onchange')
    exam_code = fields.Char(
        'Exam Session Code', size=16,
        required=True, track_visibility='onchange')
    start_date = fields.Date(
        'Start Date', required=True, track_visibility='onchange')
    end_date = fields.Date(
        'End Date', required=True, track_visibility='onchange')
    exam_ids = fields.One2many(
        'vm.exam', 'session_id', 'Exam(s)')
    exam_type = fields.Many2one(
        'vm.exam.type', 'Exam Type',
        required=True, track_visibility='onchange')
    evaluation_type = fields.Selection(
        [('normal', 'Normal'), ('grade', 'Grade')],
        'Evolution type', default="normal",
        required=True, track_visibility='onchange')
    venue = fields.Many2one(
        'res.partner', 'Venue', track_visibility='onchange')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('schedule', 'Scheduled'),
        ('held', 'Held'),
        ('cancel', 'Cancelled'),
        ('done', 'Done')
    ], 'State', default='draft', track_visibility='onchange')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_exam_session_code',
         'unique(exam_code)', 'Code should be unique per exam session!')]

    @api.constrains('start_date', 'end_date')
    def _check_date_time(self):
        if self.start_date > self.end_date:
            raise ValidationError(
                _('End Date cannot be set before Start Date.'))

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False

    def act_draft(self):
        self.state = 'draft'

    def act_schedule(self):
        self.state = 'schedule'

    def act_held(self):
        self.state = 'held'

    def act_done(self):
        self.state = 'done'

    def act_cancel(self):
        self.state = 'cancel'
