from odoo import http
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route('/viseducat_attendance/viseducat_attendance_onboarding_panel', auth='user', type='json')
    def viseducat_course_onboarding_panel(self):
        attendance = request.env['vm.attendance.register'].search([], limit=1, order="id desc")
        if attendance.attendance_onboarding_state == "closed":
            return {}

        return {
            'html': request.env.ref('viseducat_attendance.viseducat_attendance_onboarding_panel').render({
                'state': attendance.get_and_update_atendance_dashboard_onboarding_state()
            })
        }
