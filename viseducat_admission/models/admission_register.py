from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import json


class VmAdmissionRegister(models.Model):
    _name = "vm.admission.register"
    _inherit = "mail.thread"
    _description = "Admission Register"
    _order = 'id DESC'

    name = fields.Char(
        'Name', required=True, readonly=True,
        states={'draft': [('readonly', False)]})
    start_date = fields.Date(
        'Start Date', required=True, readonly=True,
        default=fields.Date.today(), states={'draft': [('readonly', False)]})
    end_date = fields.Date(
        'End Date', required=True, readonly=True,
        default=(fields.Date.today() + relativedelta(days=30)),
        states={'draft': [('readonly', False)]})
    course_id = fields.Many2one(
        'vm.course', 'Course', required=True, readonly=True,
        states={'draft': [('readonly', False)]}, track_visibility='onchange')
    min_count = fields.Integer(
        'Minimum No. of Admission', readonly=True,
        states={'draft': [('readonly', False)]})
    max_count = fields.Integer(
        'Maximum No. of Admission', readonly=True,
        states={'draft': [('readonly', False)]}, default=30)
    product_id = fields.Many2one(
        'product.product', 'Course Fees', required=True,
        domain=[('type', '=', 'service')], readonly=True,
        states={'draft': [('readonly', False)]}, track_visibility='onchange')
    admission_ids = fields.One2many(
        'vm.admission', 'register_id', 'Admissions')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirmed'),
         ('cancel', 'Cancelled'), ('application', 'Application Gathering'),
         ('admission', 'Admission Process'), ('done', 'Done')],
        'Status', default='draft', track_visibility='onchange')
    active = fields.Boolean(default=True)
    color = fields.Integer("Color Index", default=0)
    admission_count = fields.Integer(compute='admission_count_compute', string='Number of Admissions')
    kanban_admission_dashboard_graph = fields.Text(compute='_compute_dashboard_graph')

    def admission_count_compute(self):
        for record in self:
            record.admission_count = self.env['vm.admission'].search_count(
                [('register_id', '=', record.id)])

    def action_view_applications(self):
        action = self.env.ref('viseducat_admission.act_open_vm_admission_view').read()[0]
        action['domain'] = [('register_id', '=', self.id)]
        return action

    def _compute_dashboard_graph(self):
        for record in self:

            record.kanban_admission_dashboard_graph = json.dumps(record._graph_data(record.id))

    def _graph_data(self, record_id):
        x_field = 'label'
        y_field = 'value'
        vals = self.read_application_number(record_id)
        values = []
        for key, value in vals.items():
            temp_dict = {}
            temp_dict[y_field] = value
            temp_dict[x_field] = key.title()
            values.append(temp_dict)
            color = '#875A7B'
        return [{'values': values, 'area': True, 'title': '', 'key': "Application", 'color': color}]


    def read_application_number(self, record_id):
        total_draft = self.env['vm.admission'].search_count([('state', '=', 'draft'), ('register_id', '=', record_id)])
        total_done = self.env['vm.admission'].search_count([('state', '=', 'done'), ('register_id', '=', record_id)])
        vals = {
            'draft': total_draft,
            'done': total_done,

        }

        return vals

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for record in self:
            start_date = fields.Date.from_string(record.start_date)
            end_date = fields.Date.from_string(record.end_date)
            if start_date > end_date:
                raise ValidationError(
                    _("End Date cannot be set before Start Date."))

    @api.constrains('min_count', 'max_count')
    def check_no_of_admission(self):
        for record in self:
            if (record.min_count < 0) or (record.max_count < 0):
                raise ValidationError(
                    _("No of Admission should be positive!"))
            if record.min_count > record.max_count:
                raise ValidationError(_(
                    "Min Admission can't be greater than Max Admission"))

    def confirm_register(self):
        self.state = 'confirm'

    def set_to_draft(self):
        self.state = 'draft'

    def cancel_register(self):
        self.state = 'cancel'

    def start_application(self):
        self.state = 'application'

    def start_admission(self):
        self.state = 'admission'

    def close_register(self):
        self.state = 'done'
