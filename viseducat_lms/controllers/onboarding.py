from odoo import http
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route('/viseducat_lms/viseducat_lms_onboarding_panel', auth='user', type='json')
    def viseducat_lms_course_onboarding_panel(self):

        course = request.env['vm.course'].search([('online_course', '=', True)], limit=1, order="id desc")
        if course.courses_onboarding_state == "closed":
            return {}

        return {
            'html': request.env.ref('viseducat_lms.viseducat_lms_onboarding_panel').render({
                'state': course.get_and_update_lms_course_dashboard_onboarding_state()
            })
        }
