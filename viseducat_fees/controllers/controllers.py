# -*- coding: utf-8 -*-
# from odoo import http


# class ViseducatFees(http.Controller):
#     @http.route('/viseducat_fees/viseducat_fees/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viseducat_fees/viseducat_fees/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viseducat_fees.listing', {
#             'root': '/viseducat_fees/viseducat_fees',
#             'objects': http.request.env['viseducat_fees.viseducat_fees'].search([]),
#         })

#     @http.route('/viseducat_fees/viseducat_fees/objects/<model("viseducat_fees.viseducat_fees"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viseducat_fees.object', {
#             'object': obj
#         })
