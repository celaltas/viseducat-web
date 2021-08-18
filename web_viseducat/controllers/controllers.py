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

    @http.route('/comment-reply', auth='public', type="http", website=True)
    def _display_comment_res(self, **kw):

        if request.httprequest.method == 'POST':

            vals = {
            'content' :kw.get('content'),
            'comment_id': kw.get('comment_id'),
            }
            print("comment: ", vals['content'])
            if vals['content']:
                response_obj = request.env['vm.course.comment.reply'].sudo().create(vals)
                comment_obj= request.env['vm.course.comment'].sudo().search([('id', '=',kw.get('comment_id'))])
                comment_obj.write({
                    'response_ids':[(4, response_obj.id, 0)]
                })
                print("conrent res", response_obj.content)
                url = f'/course-detail?id={kw.get("course_id")}'
                return request.redirect(url)
