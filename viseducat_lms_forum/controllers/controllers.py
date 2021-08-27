# -*- coding: utf-8 -*-
# from odoo import http


# class ViseducatLmsForum(http.Controller):
#     @http.route('/viseducat_lms_forum/viseducat_lms_forum/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viseducat_lms_forum/viseducat_lms_forum/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viseducat_lms_forum.listing', {
#             'root': '/viseducat_lms_forum/viseducat_lms_forum',
#             'objects': http.request.env['viseducat_lms_forum.viseducat_lms_forum'].search([]),
#         })

#     @http.route('/viseducat_lms_forum/viseducat_lms_forum/objects/<model("viseducat_lms_forum.viseducat_lms_forum"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viseducat_lms_forum.object', {
#             'object': obj
#         })
