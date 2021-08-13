from odoo import models, fields


class VmCourse(models.Model):
    _inherit = "vm.course"

    fees_term_id = fields.Many2one('vm.fees.terms', 'Fees Term')
