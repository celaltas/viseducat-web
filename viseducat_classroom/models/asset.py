from odoo import models, fields


class VmAsset(models.Model):
    _name = "vm.asset"
    _description = "Classroom Assets"

    asset_id = fields.Many2one('vm.classroom', 'Asset')
    product_id = fields.Many2one('product.product', 'Product', required=True)
    code = fields.Char('Code', size=256)
    product_uom_qty = fields.Float('Quantity', required=True)
