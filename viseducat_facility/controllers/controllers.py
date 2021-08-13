# -*- coding: utf-8 -*-
# from odoo import http


# class ViseducatFacility(http.Controller):
#     @http.route('/viseducat_facility/viseducat_facility/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viseducat_facility/viseducat_facility/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viseducat_facility.listing', {
#             'root': '/viseducat_facility/viseducat_facility',
#             'objects': http.request.env['viseducat_facility.viseducat_facility'].search([]),
#         })

#     @http.route('/viseducat_facility/viseducat_facility/objects/<model("viseducat_facility.viseducat_facility"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viseducat_facility.object', {
#             'object': obj
#         })
