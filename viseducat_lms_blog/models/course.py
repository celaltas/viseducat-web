from odoo import models, fields


class VmBlogInherit(models.Model):
    _inherit = "vm.course"

    blog_id = fields.Many2one('blog.blog', 'Blog', readonly=True, )
    blogs_count = fields.Integer(compute='blogs_count_compute')

    def create_blog(self):
        blog_obj = self.env['blog.blog']
        blog = blog_obj.search([('name', '=', self.name)])

        if blog.exists():
            self.blog_id = blog.id
        else:
            blog_obj.create({
                'name': self.name,
            })
            self.blog_id = blog_obj.search([('name', '=', self.name)]).id


    def action_view_blogpost(self):
        action = self.env.ref('website_blog.action_blog_post').read()[0]
        action['domain'] = [('blog_id', '=', self.blog_id.id)]
        return action



    def blogs_count_compute(self):
        self.blogs_count = self.env['blog.post'].search_count([('blog_id', '=', self.blog_id.id)])
