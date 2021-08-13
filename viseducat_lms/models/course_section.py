from odoo import models, fields
from math import modf


class VmCourseMaterial(models.Model):
    _name = "vm.course.material"
    _description = "Course Section Material Line"

    course_section_id = fields.Many2one('vm.course.section', 'Section', ondelete="cascade")
    material_id = fields.Many2one('vm.material', 'Material', required=True)
    total_time = fields.Float(related='material_id.total_time', string="Total Time(HH:MM)", required=True, default=0.0)
    sequence = fields.Integer("Sequence", required=True)
    preview = fields.Boolean("Preview")


class VmCourseSection(models.Model):
    _name = "vm.course.section"
    _description = "Course Section"
    _rec_name = 'name'

    sequence = fields.Integer("Sequence", required=True)
    name = fields.Char('Section', required=True)
    total_time = fields.Float("Total Time(HH:MM)", required=True, default=0.0, compute='total_time_compute')
    material_count = fields.Integer(compute='material_count_compute')
    section_material_ids = fields.One2many('vm.course.material', 'course_section_id',
                                           'Materials',
                                           track_visibility='onchange')
    course_id = fields.Many2one('vm.course', 'Course', ondelete="cascade")

    def material_count_compute(self):
        for record in self:
            record.material_count = len(self.section_material_ids)

    def action_view_section_material(self):
        action = self.env.ref('viseducat_lms.act_open_vm_course_section_material_view').read()[0]
        action['domain'] = [('id', 'in', self.section_material_ids.ids)]
        return action

    def total_time_compute(self):
        for record in self:
            total = 0
            for rec in record.section_material_ids:
                total += rec.total_time

            record.total_time = total
