from odoo import models, fields, api, _

#
# class VmCourseDetail(models.Model):
#     _name = 'vm.course.detail'
#
#     course_id = fields.Many2one('vm.course')
#     comment_id = fields.Many2one('vm.comment')
#

class VmCourseComment(models.Model):
    _name = 'vm.course.comment'

    content = fields.Text('Comment')
    course_id = fields.Many2one('vm.course', ondelete='cascade')
    response_ids = fields.Many2many('vm.course.comment', 'vm_course_comment_rel', 'content', 'user_id', 'created_date')
