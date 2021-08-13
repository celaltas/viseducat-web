from odoo import models, fields


class VmGradeConfiguration(models.Model):
    _name = "vm.grade.configuration"
    _rec_name = "result"
    _description = "Grade Configuration"

    min_per = fields.Integer('Minimum Percentage', required=True)
    max_per = fields.Integer('Maximum Percentage', required=True)
    result = fields.Char('Result to Display', required=True)
