from odoo import models, fields


class VmStudent(models.Model):
    _inherit = "vm.student"

    library_card_id = fields.Many2one('vm.library.card', 'Library Card')
    media_movement_lines = fields.One2many(
        'vm.media.movement', 'student_id', 'Movements')