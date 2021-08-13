# -*- coding: utf-8 -*-
# from odoo import http


# class ViseducatActivity(http.Controller):
#     @http.route('/viseducat_activity/viseducat_activity/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viseducat_activity/viseducat_activity/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viseducat_activity.listing', {
#             'root': '/viseducat_activity/viseducat_activity',
#             'objects': http.request.env['viseducat_activity.viseducat_activity'].search([]),
#         })

#     @http.route('/viseducat_activity/viseducat_activity/objects/<model("viseducat_activity.viseducat_activity"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viseducat_activity.object', {
#             'object': obj
#         })
