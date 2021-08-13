from odoo import models, fields, api, _
from babel.dates import format_date
import json
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class VmBatch(models.Model):
    _name = "vm.batch"
    _inherit = "mail.thread"
    _description = "Batch"

    code = fields.Char('Code', size=16, required=True)
    name = fields.Char('Name', size=32, required=True)
    start_date = fields.Date(
        'Start Date', required=True, default=fields.Date.today())
    end_date = fields.Date('End Date', required=True)
    course_id = fields.Many2one('vm.course', 'Course', required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer("Color Index", default=0)
    student_count = fields.Integer(compute='student_count_compute', string='Number of Student')
    dashboard_graph_data = fields.Text(compute='_compute_dashboard_graph')

    _sql_constraints = [
        ('unique_batch_code',
         'unique(code)', 'Code should be unique per batch!')]

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for rec in self:
            if rec.start_date >= rec.end_date:
                raise ValidationError(
                    _("End date cannot be set before start date."))

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self.env.context.get('get_parent_batch', False):
            lst = []
            lst.append(self.env.context.get('course_id'))
            courses = self.env['vm.course'].browse(lst)
            while courses.parent_id:
                lst.append(courses.parent_id.id)
                courses = courses.parent_id
            batches = self.env['vm.batch'].search([('course_id', 'in', lst)])
            return batches.name_get()
        return super(VmBatch, self).name_search(
            name, args, operator=operator, limit=limit)


    def _compute_dashboard_graph(self):
        for record in self:
            record.dashboard_graph_data = json.dumps(record._graph_data(record.id))

    def read_total_present(self, record_id, dates):
        records = []
        for date in dates:
            total_present = self.env['vm.attendance.line'].search_count(
                [('present', '=', True), ('batch_id', '=', record_id), ('attendance_date', '=', date)])
            records.append(total_present)
        return records

    def _get_weekdays(self):

        current_day = date.today()
        weekday = current_day.isoweekday()
        start = current_day - timedelta(days=weekday)
        dates = [(start + timedelta(days=d)) for d in range(7)]
        return dates

    def _graph_data(self, record_id):
        locale = self._context.get('lang') or 'en_US'
        dates = self._get_weekdays()
        week_days = []
        for date in dates:
            formatted_day_name = format_date(date, locale=locale).split(',')
            week_days.append(formatted_day_name[0])

        x_field = 'label'
        y_field = 'value'

        record_data = self.read_total_present(record_id, dates)
        values = []
        for day, present in zip(week_days, record_data):
            temp_dict = {}
            temp_dict[y_field] = present
            temp_dict[x_field] = day
            values.append(temp_dict)

        return [{'values': values, 'area': True, 'title': '', 'key': "Attendance", 'color': '#7c7bad'}]

    def student_count_compute(self):
        for record in self:
            record.student_count = self.env['vm.student'].search_count(
                [('course_detail_ids.batch_id', '=', record.id)])

    def action_open_vm_student_view(self):
        action = self.env.ref('viseducat_core.act_open_vm_student_view_2').read()[0]
        action['domain'] = [('course_detail_ids.batch_id', '=', self.id)]

        return action


    def action_save_onboarding_batch_step(self):
        course =self.env['vm.course'].search([], limit=1, order="id desc")
        course.sudo().set_onboarding_step_done('course_onboarding_batch_layout_state')


    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Batch'),
            'template': '/viseducat_core/static/xls/vm_batch.xls'
        }]
