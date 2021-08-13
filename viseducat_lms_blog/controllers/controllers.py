# -*- coding: utf-8 -*-
# from odoo import http


# class ViseducatLmsBlog(http.Controller):
#     @http.route('/viseducat_lms_blog/viseducat_lms_blog/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viseducat_lms_blog/viseducat_lms_blog/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viseducat_lms_blog.listing', {
#             'root': '/viseducat_lms_blog/viseducat_lms_blog',
#             'objects': http.request.env['viseducat_lms_blog.viseducat_lms_blog'].search([]),
#         })

#     @http.route('/viseducat_lms_blog/viseducat_lms_blog/objects/<model("viseducat_lms_blog.viseducat_lms_blog"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viseducat_lms_blog.object', {
#             'object': obj
#         })
