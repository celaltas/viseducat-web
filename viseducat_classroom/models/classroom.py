from odoo import models, fields, api


class VmClassroom(models.Model):
    _name = "vm.classroom"
    _description = "Classroom"

    name = fields.Char('Name', size=16, required=True)
    code = fields.Char('Code', size=16, required=True)
    course_id = fields.Many2one('vm.course', 'Course')
    batch_id = fields.Many2one('vm.batch', 'Batch')
    capacity = fields.Integer(string='No of Person')
    facilities = fields.One2many('vm.facility.line', 'classroom_id',
                                 string='Facility Lines')
    asset_line = fields.One2many('vm.asset', 'asset_id',
                                 string='Asset')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_classroom_code',
         'unique(code)', 'Code should be unique per classroom!')]

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False

