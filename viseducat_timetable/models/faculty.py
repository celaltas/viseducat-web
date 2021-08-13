from odoo import models, fields


class VmFaculty(models.Model):
    _inherit = "vm.faculty"

    session_ids = fields.One2many('vm.session', 'faculty_id', 'Sessions')

