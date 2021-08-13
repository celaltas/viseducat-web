from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentMigrate(models.TransientModel):
    """Student Migration Wizard"""
    _name = "student.migrate"
    _description = "Student Migrate"

    date = fields.Date('Date', required=True, default=fields.Date.today())
    course_from_id = fields.Many2one('vm.course', 'From Course', required=True)
    course_to_id = fields.Many2one('vm.course', 'To Course', required=True)
    batch_id = fields.Many2one('vm.batch', 'To Batch')
    optional_sub = fields.Boolean("Optional Subjects")
    student_ids = fields.Many2many(
        'vm.student', string='Student(s)', required=True)

    @api.constrains('course_from_id', 'course_to_id')
    def _check_admission_register(self):
        for rec in self:
            if rec.course_from_id == rec.course_to_id:
                raise ValidationError(_("From course must not be same as to course!"))

            if rec.course_from_id.parent_id:
                if rec.course_from_id.parent_id != rec.course_to_id.parent_id:
                    raise ValidationError(_("Can't migrate, As selected courses don't  share same parent course!"))
            else:
                raise ValidationError(_("Can't migrate, Proceed for new admission"))

    @api.onchange('course_from_id')
    def onchange_course_id(self):
        self.student_ids = False

    def student_migrate_forward(self):
        act_type = self.env['vm.activity.type'].search([('name', 'ilike', 'migration')])
        for rec in self:
            for student in rec.student_ids:
                activity_vals = {
                    'student_id': student.id,
                    'type_id': act_type.id,
                    'date': self.date,
                    'description': 'Migration From' +
                                   rec.course_from_id.name +
                                   ' to ' + rec.course_to_id.name

                }
            self.env['vm.activity'].create(activity_vals)
            student_course = self.env['vm.student.course'].search(
                [('student_id', '=', student.id), ('course_id', '=', rec.course_from_id.id)])
            student_course.write({
                'course_id': rec.course_to_id.id,
                'batch_id': rec.batch_id.id
            })

            reg_id = self.env['vm.subject.registration'].create({
                'student_id': student.id,
                'batch_id': rec.batch_id.id,
                'course_id': rec.course_to_id.id,
                'min_unit_load': rec.course_to_id.min_unit_load or 0.0,
                'max_unit_load': rec.course_to_id.max_unit_load or 0.0,
                'state': 'draft',
            })
            reg_id.get_subjects()

            reg_id.get_subjects()
            if not rec.optional_sub:
                reg_id.action_submitted()
                reg_id.action_approve()
