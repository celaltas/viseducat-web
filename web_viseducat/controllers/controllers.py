from odoo import http, fields,_
from odoo.http import request
from datetime import datetime



class ViseducatOnline(http.Controller):

    @http.route('/courses', auth='public', type="http", website=True)
    def _display_courses(self, **kw):
        categories = request.env['vm.course.category'].sudo().search([])
        courses = request.env['vm.course'].sudo().search(
            [('online_course', '=', True), ('state', '=', 'open')])
        vals = {
            'categories': categories,
            'courses': courses,
        }
        return request.render('web_viseducat.display_courses', vals)

    @http.route('/course-detail', auth='public', type="http", website=True)
    def _display_courses_detail(self, **kw):
        if request.httprequest.method == 'POST':

            vals = {
                'content': kw.get('content'),
                'course_id': kw.get('id'),

            }
            if len(vals['content'])>3:
                
                comment_obj = request.env['vm.course.comment'].sudo().create(vals)
                url = f'/course-detail?id={kw.get("id")}'
                return request.redirect(url)

            else:

                raise ValueError("3 ten küçük olamaz")


        else:
            vals = {}
            course_obj = request.env['vm.course'].sudo().search(
                [('id', '=', kw.get('id'))])
            comment_obj_list = request.env['vm.course.comment'].sudo().search(
                [('course_id', '=', course_obj.id)])
            vals.update({
                'course': course_obj,
                'comments': comment_obj_list,
            })
            return request.render('web_viseducat.display_course_details', vals)

    @http.route('/comment-reply', auth='public', type="http", website=True)
    def _display_comment_res(self, **kw):
        
        if request.httprequest.method == 'POST':
            
            vals = {
                'content': kw.get('content'),
                'comment_id': kw.get('comment_id'),
            }
            if len(vals['content'])>3:
                print(vals['content'])
                response_obj = request.env['vm.course.comment.reply'].sudo().create(
                    vals)
                comment_obj = request.env['vm.course.comment'].sudo().search(
                    [('id', '=', kw.get('comment_id'))])
                comment_obj.write({
                    'response_ids': [(4, response_obj.id, 0)]
                })
                url = f'/course-detail?id={kw.get("course_id")}'
                return request.redirect(url)
            else:
                
                raise ValueError(_("Error"))
                
       



    @http.route('/delete', type='json', auth='user', website=True, csrf=False)
    def _delete_comment_reply(self, **kw):

        response_obj = request.env['vm.course.comment.reply'].sudo().search(
            [('id', '=', kw.get('id'))])
        res = {
            'result':False
        }
        if response_obj:
            response_obj.unlink()
            res['result'] = True
            
        return res



    @http.route('/edit', type='json', auth='user', website=True, csrf=False)
    def _edit_comment_reply(self, **kw):

        response_obj = request.env['vm.course.comment.reply'].sudo().search(
            [('id', '=', kw.get('id'))])

        res = {
            'result':False
        }

        if response_obj:
            text=kw.get('text')
            if len(text)>3:
                response_obj.write({
                    'content': text
                })
                res['result'] = True

            else:
                raise ValueError("Sikerler")            
        return res
