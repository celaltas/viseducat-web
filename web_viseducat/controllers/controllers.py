from odoo import http, fields
from odoo.http import request


class ViseducatOnline(http.Controller):


    @http.route('/courses', auth='public', type="http", website=True)
    def _display_courses(self, **kw):
        categories = request.env['vm.course.category'].sudo().search([])
        courses = request.env['vm.course'].sudo().search([('online_course', '=', True), ('state', '=', 'open')])
        vals = {
            'categories': categories,
            'courses': courses,
        }
        return request.render('web_viseducat.display_courses', vals)

    @http.route('/course-detail', auth='public', type="http", website=True)
    def enroll_course(self, **kw):
        vals = {}
        course_obj = request.env['vm.course'].search([('id', '=', kw.get('id'))])
        vals.update({
            'course': course_obj,
        })

        return request.render('web_viseducat.display_course_details', vals)
