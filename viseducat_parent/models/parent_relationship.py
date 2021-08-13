from odoo import models, fields


class VmParentRelation(models.Model):
    _name = "vm.parent.relationship"
    _description = "Relationships"

    name = fields.Char('Name', required=True)
