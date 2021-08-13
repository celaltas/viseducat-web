from odoo import models, fields, api, _
from odoo import exceptions


class VmMediaPurchase(models.Model):
    _name = "vm.media.purchase"
    _inherit = "mail.thread"
    _description = "Media Purchase Request"

    name = fields.Char('Title', size=128, required=True)
    author = fields.Char(
        'Author(s)', size=256, required=True, track_visibility='onchange')
    edition = fields.Char('Edition')
    publisher = fields.Char('Publisher(s)', size=256)
    course_ids = fields.Many2one(
        'vm.course', 'Course', required=True, track_visibility='onchange')
    subject_ids = fields.Many2one(
        'vm.subject', 'Subject', required=True, track_visibility='onchange')
    requested_id = fields.Many2one(
        'res.partner', 'Requested By',
        default=lambda self: self.env.user.partner_id.id)
    state = fields.Selection(
        [('draft', 'Draft'), ('request', 'Requested'),
         ('reject', 'Rejected'), ('accept', 'Accepted')],
        'State', readonly=True, default='draft', track_visibility='onchange')
    media_type_id = fields.Many2one('vm.media.type', 'Media Type')
    active = fields.Boolean(default=True)

    def act_requested(self):
        self.state = 'request'

    def act_accept(self):
        self.state = 'accept'

    def act_reject(self):
        self.state = 'reject'

    @api.model
    def create(self, vals):
        if self.env.user.child_ids:
            raise exceptions.Warning(_('Invalid Action!\n Parent can not create \
            Media Purchase Requests!'))
        return super(VmMediaPurchase, self).create(vals)

    def write(self, vals):
        if self.env.user.child_ids:
            raise exceptions.Warning(_('Invalid Action!\n Parent can not edit \
            Media Purchase Requests!'))
        return super(VmMediaPurchase, self).write(vals)