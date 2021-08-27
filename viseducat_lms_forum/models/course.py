from odoo import models, fields


class VmForumInherit(models.Model):
    _inherit = "vm.course"

    forum_id = fields.Many2one('forum.forum', 'Forum', readonly=True, )
    forum_count = fields.Integer(compute='forum_count_compute')




    def create_forum(self):
        pass
        # blog_obj = self.env['blog.blog']
        # blog_obj.create({
        #     'name': self.name,
        # })
        # self.blog_id = blog_obj.search([('name', '=', self.name)]).id


    def action_view_forumpost(self):
        pass
        # action = self.env.ref('website_blog.action_blog_post').read()[0]
        # action['domain'] = [('blog_id', '=', self.blog_id.id)]
        # return action



    def forum_count_compute(self):
        pass
        self.forum_count = 2
