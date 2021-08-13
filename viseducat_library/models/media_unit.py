from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VmMediaUnit(models.Model):
    _name = "vm.media.unit"
    _inherit = "mail.thread"
    _description = "Media Unit"
    _order = "name"

    name = fields.Char('Name', required=True)
    media_id = fields.Many2one('vm.media', 'Media',
                               required=True, track_visibility='onchange')
    barcode = fields.Char('Barcode', size=20)
    movement_lines = fields.One2many(
        'vm.media.movement', 'media_unit_id', 'Movements')
    state = fields.Selection(
        [('available', 'Available'), ('issue', 'Issued')],
        'State', default='available', track_visibility='onchange')
    media_type_id = fields.Many2one(related='media_id.media_type_id',
                                    store=True, string='Media Type')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_name_barcode',
         'unique(barcode)',
         'Barcode must be unique per Media unit!'),
    ]

    @api.model
    def create(self, vals_list):
        barcode = self.env['ir.sequence'].next_by_code('vm.media.unit') or 'New'
        vals_list['barcode'] = barcode
        res = super(VmMediaUnit, self).create(vals_list)
        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        records = self.browse()
        if name:
            records = self.search([('name', operator, name)] + args, limit=limit)
        if not records:
            records = self.search([('barcode', operator, name)] + args, limit=limit)
        return records.name_get()
