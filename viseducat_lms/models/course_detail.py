from odoo import models, fields, api, _

class VmCourseCommentReply(models.Model):
    _name = 'vm.course.comment.reply'

    content = fields.Text('Comment')
    comment_id = fields.Many2one('vm.course.comment', ondelete='cascade')
    








class VmCourseComment(models.Model):
    _name = 'vm.course.comment'

    content = fields.Text('Comment')
    course_id = fields.Many2one('vm.course', ondelete='cascade')
    response_ids = fields.Many2many('vm.course.comment.reply', string='Comment Response')
