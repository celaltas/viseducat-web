from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VmAssignmentSubLine(models.Model):
    _name = "vm.assignment.sub.line"
    _inherit = "mail.thread"
    _rec_name = "assignment_id"
    _description = "Assignment Submission"
    _order = "submission_date DESC"

    # def _compute_get_user_group(self):
    #     for user in self:
    #         if self.env.user.has_group(
    #                 'viseducat_core.group_vm_back_office_admin') or \
    #                 self.env.user.has_group(
    #                     'viseducat_core.group_vm_back_office') or \
    #                 self.env.user.has_group(
    #                     'viseducat_core.group_vm_faculty'):
    #             user.user_boolean = True
    #         else:
    #             user.user_boolean = False

    def _compute_get_user_group(self):
        for user in self:
            user.user_boolean = True


    assignment_id = fields.Many2one(
        'vm.assignment', 'Assignment', required=True)
    student_id = fields.Many2one(
        'vm.student', 'Student',
        default=lambda self: self.env['vm.student'].search(
            [('user_id', '=', self.env.user.id)]), required=True)
    description = fields.Text('Description', track_visibility='onchange')
    state = fields.Selection([
        ('draft', 'Draft'), ('submit', 'Submitted'), ('reject', 'Rejected'),
        ('change', 'Change Req.'), ('accept', 'Accepted')], basestring='State',
        default='draft', track_visibility='onchange')
    submission_date = fields.Datetime(
        'Submission Date', readonly=True,
        default=lambda self: fields.Datetime.now(), required=True)
    marks = fields.Float('Marks', track_visibility='onchange')
    note = fields.Text('Note')
    user_id = fields.Many2one(
        'res.users', related='student_id.user_id', string='User')
    faculty_user_id = fields.Many2one(
        'res.users', related='assignment_id.faculty_id.user_id',
        string='Faculty User')
    user_boolean = fields.Boolean(string='Check user',
                                  compute='_compute_get_user_group')
    active = fields.Boolean(default=True)

    def act_draft(self):
        result = self.state = 'draft'
        return result and result or False

    def act_submit(self):
        result = self.state = 'submit'
        return result and result or False

    def act_accept(self):
        result = self.state = 'accept'
        return result and result or False

    def act_change_req(self):
        result = self.state = 'change'
        return result and result or False

    def act_reject(self):
        result = self.state = 'reject'
        return result and result or False

    # def unlink(self):
    #     for record in self:
    #         if not record.state == 'draft' and not self.env.user.has_group(
    #                 'viseducat_core.group_vm_faculty'):
    #             raise ValidationError(
    #                 _("You can't delete none draft submissions!"))
    #     res = super(VmAssignmentSubLine, self).unlink()
    #     return res
    #
    @api.model
    def create(self, vals):
        if self.env.user.child_ids:
            raise Warning(_('Invalid Action!\n Parent can not \
            create Assignment Submissions!'))
        return super(VmAssignmentSubLine, self).create(vals)

    def write(self, vals):
        if self.env.user.child_ids:
            raise Warning(_('Invalid Action!\n Parent can not edit \
            Assignment Submissions!'))
        return super(VmAssignmentSubLine, self).write(vals)

