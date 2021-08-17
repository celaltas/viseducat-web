from odoo import http, fields
from odoo.http import request
from datetime import datetime


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
    def _display_courses_detail(self, **kw):
        if request.httprequest.method == 'POST':

            vals = {
                    'content' :kw.get('content'),
                    'course_id': kw.get('id'),

            }
            comment_obj = request.env['vm.course.comment'].sudo().create(vals)
            url = f'/course-detail?id={kw.get("id")}'
            return request.redirect(url)


        else:
            vals = {}
            course_obj = request.env['vm.course'].sudo().search([('id', '=', kw.get('id'))])
            comment_obj_list = request.env['vm.course.comment'].sudo().search([('course_id', '=', course_obj.id)])
            vals.update({
                'course': course_obj,
                'comments': comment_obj_list,
            })
            return request.render('web_viseducat.display_course_details', vals)
