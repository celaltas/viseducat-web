from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.web import \
    Home as home


class ViseducatHome(home):

    @http.route()
    def web_login(self, redirect=None, *args, **kw):
        response = super(ViseducatHome, self).web_login(
            redirect=redirect, *args, **kw)
        if not redirect and request.params['login_success']:
            if request.env['res.users'].browse(request.uid).has_group(
                    'base.group_user'):
                redirect = b'/web?' + request.httprequest.query_string
            else:
                if request.env.user.is_parent:
                    redirect = '/my/child'
                else:
                    redirect = '/my/home'
            return http.redirect_with_hash(redirect)
        return response

    def _login_redirect(self, uid, redirect=None):
        if request.env.user.is_parent:
            return '/my/child'
        return '/my/home'

