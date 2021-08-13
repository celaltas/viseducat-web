from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VmExamAttendees(models.Model):
    _name = "vm.exam.attendees"
    _rec_name = "student_id"
    _description = "Exam Attendees"

    student_id = fields.Many2one('vm.student', 'Student', required=True)
    status = fields.Selection(
        [('present', 'Present'), ('absent', 'Absent')],
        'Status', default="present", required=True)
    marks = fields.Integer('Marks')
    note = fields.Text('Note')
    exam_id = fields.Many2one(
        'vm.exam', 'Exam', required=True, ondelete="cascade")
    course_id = fields.Many2one('vm.course', 'Course', readonly=True)
    batch_id = fields.Many2one('vm.batch', 'Batch', readonly=True)
    room_id = fields.Many2one('vm.exam.room', 'Room')

    _sql_constraints = [
        ('unique_attendees',
         'unique(student_id,exam_id)',
         'Attendee must be unique per exam.'),
    ]

    @api.onchange('exam_id')
    def onchange_exam(self):
        self.course_id = self.exam_id.session_id.course_id
        self.batch_id = self.exam_id.session_id.batch_id
        self.student_id = False

    @api.constrains('marks')
    def _check_marks(self):
        if self.marks < 0.0:
            raise ValidationError(_("Enter proper marks!"))

    @api.onchange('marks')
    def onchange_marks(self):
        if self.status == "absent" and self.marks > 0:
            raise ValidationError(_("The mark must be zero when there is no student!"))

    @api.constrains('status')
    def _check_marks(self):
        if self.status == "absent":
            self.marks = 0.0

