from odoo import models, fields


class VmFacilityLine(models.Model):
    _inherit = "vm.facility.line"

    classroom_id = fields.Many2one('vm.classroom', 'Classroom')
