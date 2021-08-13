
from odoo import models, fields


class VmTag(models.Model):
    _name = "vm.tag"
    _description = "Media Tags"

    name = fields.Char('Name', size=64, required=True)