from odoo import http, fields, _
from odoo.http import request
from datetime import datetime


class ViseducatOnline(http.Controller):
    _post_per_page = 2

    @http.route(['/courses',
                '/courses/page/<int:page>',
    ], auth='public', type="http", website=True)
    def _display_courses(self, category_filter='all', search='', price_filters='all', page=1, **kw):

        course_obj = request.env['vm.course']

        url_args = {
            category_filter : 'all',
            price_filters: 'all',
        }

        domain = [('online_course', '=', True), ('state', '=', 'open')]

        if search:
            url_args['search'] = search
            domain += ['|','|', '|', ('user_id.name', 'ilike', search),('name', 'ilike', search), ('short_description','ilike', search),('full_description','ilike', search)]

        if category_filter == 'all':
            categories = request.env['vm.course.category'].sudo().search([])
            domain += [('category_ids', 'in', categories.ids)]
        else:
            category = request.env['vm.course.category'].sudo().search(
                [('name', '=', category_filter)])
            domain += [('category_ids', 'in', category.id)]

        # Type çözülmeli
        # if price_filters == 'unanswered':
        #     domain += [('type', '=', price_filters)]
        
        print("domain:" ,domain)

        total = course_obj.search_count(domain)

        pager = request.website.pager(
            url='/courses',
            total=total,
            page=page,
            step=self._post_per_page,
            scope=self._post_per_page,
            url_args=url_args
        )

        course_ids = course_obj.search(domain, limit=self._post_per_page, offset=pager['offset'])
        categories = request.env['vm.course.category'].sudo().search([])
        vals = {
            'categories': categories,
            'courses': course_ids,
            'category_filter': category_filter,
            'price_filters': price_filters,
            'search': search,
            'pager': pager,

        }
        return request.render('web_viseducat.display_courses', vals)

    @http.route('/course-detail', auth='public', type="http", website=True)
    def _display_courses_detail(self, **kw):
        if request.httprequest.method == 'POST':

            vals = {
                'content': kw.get('content'),
                'course_id': kw.get('id'),

            }
            if len(vals['content']) > 3:

                comment_obj = request.env['vm.course.comment'].sudo().create(
                    vals)
                url = f'/course-detail?id={kw.get("id")}'
                return request.redirect(url)

            else:

                raise ValueError("3 ten küçük olamaz")

        else:
            vals = {}
            course_obj = request.env['vm.course'].sudo().search(
                [('id', '=', kw.get('id'))])
            forum_posts = request.env['forum.post'].sudo().search(
                [('forum_id', '=', course_obj.forum_id.id)])
            comment_obj_list = request.env['vm.course.comment'].sudo().search(
                [('course_id', '=', course_obj.id)])
            vals.update({
                'course': course_obj,
                'comments': comment_obj_list,
                'posts': forum_posts,
            })
            return request.render('web_viseducat.display_course_details', vals)

    @http.route('/comment-reply', auth='public', type="http", website=True)
    def _display_comment_res(self, **kw):

        if request.httprequest.method == 'POST':

            vals = {
                'content': kw.get('content'),
                'comment_id': kw.get('comment_id'),
            }
            if len(vals['content']) > 3:
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
            'result': False
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
            'result': False
        }

        if response_obj:
            text = kw.get('text')
            if len(text) > 3:
                response_obj.write({
                    'content': text
                })
                res['result'] = True

            else:
                raise ValueError("Value Error")
        return res
    
    @http.route('/registration', type='http', auth='public', website=True)
    def _display_registration(self, **kw):
        return request.render('web_viseducat.display_registration')


    @http.route('/payment', type='http', auth='public', website=True)
    def _display_payment(self, **kw):
        return request.render('web_viseducat.display_payment')

    @http.route('/cart', type='http', auth='public', website=True)
    def _display_cart(self, **kw):
        return request.render('web_viseducat.display_cart')

    @http.route('/confirmation', type='http', auth='public', website=True)
    def _display_confirmation(self, **kw):
        return request.render('web_viseducat.display_confirmation')

    @http.route('/confirm_order', type='http', auth='public', website=True)
    def _display_confirm_order(self, **kw):
        return request.render('web_viseducat.display_confirm_order')

    @http.route('/documents', type='http', auth='public', website=True)
    def _display_documents(self, **kw):
        return request.render('web_viseducat.display_documents')

