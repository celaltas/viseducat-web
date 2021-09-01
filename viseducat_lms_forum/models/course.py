from odoo import models, fields


class VmForumInherit(models.Model):
    _inherit = "vm.course"

    forum_id = fields.Many2one('forum.forum', 'Forum', readonly=True, )
    forum_count = fields.Integer(compute='forum_count_compute')




    def create_forum(self):
        forum_obj = self.env['forum.forum']
        forum_obj.create({
            'name': self.name,
            'image_1920': self.image_1920 or None,
        })
        self.forum_id = forum_obj.search([('name', '=', self.name)]).id


    def action_view_forumpost(self):
        action = self.env.ref('website_forum.action_forum_post').read()[0]
        action['domain'] = [('forum_id', '=', self.forum_id.id)]
        return action



    def forum_count_compute(self):
        self.forum_count = self.env['forum.post'].search_count([('forum_id', '=', self.forum_id.id)])
