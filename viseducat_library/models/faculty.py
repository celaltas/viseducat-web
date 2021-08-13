from odoo import models, fields


class VmFaculty(models.Model):
    _inherit = "vm.faculty"

    library_card_id = fields.Many2one('vm.library.card', 'Library Card')
    media_movement_lines = fields.One2many(
        'vm.media.movement', 'faculty_id', 'Movements')