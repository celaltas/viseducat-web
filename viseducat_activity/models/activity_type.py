from odoo import models, fields


class VmActivityType(models.Model):
    _name = "vm.activity.type"
    _description = "Activity Type"

    name = fields.Char('Name', size=128, required=True)
    active = fields.Boolean(default=True)
