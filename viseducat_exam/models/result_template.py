from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VmResultTemplate(models.Model):
    _name = "vm.result.template"
    _inherit = ["mail.thread"]
    _description = "Result Template"

    exam_session_id = fields.Many2one(
        'vm.exam.session', 'Exam Session',
        required=True, track_visibility='onchange')
    evaluation_type = fields.Selection(
        related='exam_session_id.evaluation_type',
        store=True, track_visibility='onchange')
    name = fields.Char("Name", size=254,
                       required=True, track_visibility='onchange')
    result_date = fields.Date(
        'Result Date', required=True,
        default=fields.Date.today(), track_visibility='onchange')
    grade_ids = fields.Many2many(
        'vm.grade.configuration', string='Grade Configuration')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('result_generated', 'Result Generated')
    ], string='State', default='draft', track_visibility='onchange')
    active = fields.Boolean(default=True)

    @api.constrains('exam_session_id')
    def _check_exam_session(self):
        for record in self:
            for exam in record.exam_session_id.exam_ids:
                if exam.state != 'done':
                    raise ValidationError(_('All subject exam should be done.'))

    @api.constrains('grade_ids')
    def _check_min_max_per(self):
        for record in self:
            count = 0
            for grade in record.grade_ids:
                for sub_grade in record.grade_ids:
                    if grade != sub_grade:
                        if (sub_grade.min_per <= grade.min_per and
                            sub_grade.max_per >= grade.min_per) or \
                                (sub_grade.min_per <= grade.max_per and
                                 sub_grade.max_per >= grade.max_per):
                            count += 1
            if count > 0:
                raise ValidationError(
                    _('Percentage range conflict with other record.'))

    def generate_result(self):
        for record in self:
            marksheet_reg_id = self.env['vm.marksheet.register'].create({
                'name': 'Mark Sheet for %s' % record.exam_session_id.name,
                'exam_session_id': record.exam_session_id.id,
                'generated_date': fields.Date.today(),
                'generated_by': self.env.uid,
                'state': 'draft',
                'result_template_id': record.id
            })
            student_dict = {}
            for exam in record.exam_session_id.exam_ids:
                for attendee in exam.attendees_line:
                    result_line_id = self.env['vm.result.line'].create({
                        'student_id': attendee.student_id.id,
                        'exam_id': exam.id,
                        'marks': str(attendee.marks and attendee.marks or 0),
                    })
                    if attendee.student_id.id not in student_dict:
                        student_dict[attendee.student_id.id] = []
                    student_dict[attendee.student_id.id].append(result_line_id)
            for student in student_dict:
                marksheet_line_id = self.env['vm.marksheet.line'].create({
                    'student_id': student,
                    'marksheet_reg_id': marksheet_reg_id.id,
                })
                for result_line in student_dict[student]:
                    result_line.marksheet_line_id = marksheet_line_id
            record.state = 'result_generated'
