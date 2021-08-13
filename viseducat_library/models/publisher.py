from odoo import models, fields


class VmPublisher(models.Model):
    _name = "vm.publisher"
    _description = "Publisher"

    name = fields.Char('Name', size=20, required=True)
    address_id = fields.Many2one('res.partner', 'Address')
    media_ids = fields.Many2many('vm.media', string='Media(s)')


    def action_save_onboarding_publisher_step(self):
        library = self.env['vm.media.type'].search([], limit=1, order="id desc")
        library.sudo().set_onboarding_step_done('library_onboarding_publisher_layout_state')