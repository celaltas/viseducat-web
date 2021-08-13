from datetime import timedelta, date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class VmMediaMovement(models.Model):
    _name = "vm.media.movement"
    _inherit = "mail.thread"
    _description = "Media Movement"
    _rec_name = "media_id"
    _order = "return_date DESC"

    media_id = fields.Many2one('vm.media', 'Media', required=True)
    media_unit_id = fields.Many2one(
        'vm.media.unit', 'Media Unit', required=True,
        track_visibility='onchange', domain=[('state', '=', 'available')])
    type = fields.Selection(
        [('student', 'Student'), ('faculty', 'Faculty')],
        'Student/Faculty', required=True)
    student_id = fields.Many2one('vm.student', 'Student')
    faculty_id = fields.Many2one('vm.faculty', 'Faculty')
    library_card_id = fields.Many2one(
        'vm.library.card', 'Library Card', required=True,
        track_visibility='onchange')
    issued_date = fields.Date(
        'Issued Date', track_visibility='onchange',
        required=True, default=fields.Date.today())
    return_date = fields.Date('Due Date', required=True)
    actual_return_date = fields.Date('Actual Return Date')
    penalty = fields.Float('Penalty', compute='calculate_penalty')
    partner_id = fields.Many2one(
        'res.partner', 'Person', track_visibility='onchange')
    reserver_name = fields.Char('Person Name', size=256)
    state = fields.Selection(
        [('available', 'Available'), ('reserve', 'Reserved'),
         ('issue', 'Issued'), ('lost', 'Lost'),
         ('return', 'Returned'), ('return_done', 'Returned Done')],
        'Status', default='available', track_visibility='onchange')
    media_type_id = fields.Many2one(related='media_id.media_type_id',
                                    store=True, string='Media Type')
    user_id = fields.Many2one(
        'res.users', string='Users')
    invoice_id = fields.Many2one('account.move', 'Invoice', readonly=True)
    active = fields.Boolean(default=True)

    @api.constrains('issued_date', 'return_date')
    def _check_date(self):
        if self.issued_date > self.return_date:
            raise ValidationError(_(
                'Return Date cannot be set before Issued Date.'))

    @api.constrains('issued_date', 'actual_return_date')
    def check_actual_return_date(self):
        if self.actual_return_date:
            if self.issued_date > self.actual_return_date:
                raise ValidationError(_(
                    'Actual Return Date cannot be set before Issued Date'))

    @api.onchange('library_card_id')
    def onchange_library_card_id(self):
        self.type = self.library_card_id.type
        self.return_date = self.issued_date + timedelta(
            days=self.library_card_id.library_card_type_id.duration)
        if self.type == 'student':
            self.student_id = self.library_card_id.student_id.id or False
            self.partner_id = self.student_id.partner_id.id or False
            self.user_id = self.student_id.user_id.id or False
        else:
            self.faculty_id = self.library_card_id.faculty_id.id or False
            self.partner_id = self.faculty_id.partner_id.id or False
            self.user_id = self.faculty_id.user_id.id or False

    @api.onchange('media_unit_id')
    def change_media_unit_id(self):
        self.state = self.media_unit_id.state
        self.media_id = self.media_unit_id.media_id

    def issue_media(self):
        for rec in self:
            if rec.media_unit_id:
                rec.media_unit_id.state = 'issue'
                rec.state = 'issue'

    def return_media(self, return_date):
        for rec in self:
            if not return_date:
                return_date = date.today()
            rec.actual_return_date = return_date
            rec.calculate_penalty()
            if rec.penalty > 0.0:
                rec.state = 'return'
            else:
                rec.state = 'return_done'
            rec.media_unit_id.state = 'available'

    def calculate_penalty(self):
        for rec in self:
            if rec.actual_return_date != False:
                penalty_days = int((rec.actual_return_date - rec.return_date).days)
                if penalty_days > 0:
                    x = rec.library_card_id.library_card_type_id
                    penalty_amt = penalty_days * x.penalty_amt_per_day
                    rec.penalty = penalty_amt
                else:
                    rec.penalty = 0

            else:
                rec.penalty = 0

    def create_penalty_invoice(self):
        for rec in self:
            account_id = False
            product = self.env.ref('viseducat_library.vm_product_7')
            if product.id:
                account_id = product.property_account_income_id.id
            if not account_id:
                account_id = \
                    product.categ_id.property_account_income_categ_id.id
            if not account_id:
                raise UserError(
                    _('There is no income account defined for this \
                    product: "%s". You may have to install a chart of \
                    account from Accounting app, settings \
                    menu.') % (product.name,))

            invoice = self.env['account.move'].create({
                'partner_id': rec.student_id.partner_id.id,
                'type': 'out_invoice',
                'invoice_date': fields.Date.today(),
            })
            line_values = {'name': product.name,
                           'account_id': account_id,
                           'price_unit': rec.penalty,
                           'quantity': 1.0,
                           'discount': 0.0,
                           'product_uom_id': product.uom_id.id,
                           'product_id': product.id, }
            invoice.write({'invoice_line_ids': [(0, 0, line_values)]})

            invoice._compute_invoice_taxes_by_group()
            #           invoice.action_invoice_open()
            self.invoice_id = invoice.id


