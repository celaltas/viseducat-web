from odoo import http
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route('/viseducat_library/viseducat_library_onboarding_panel', auth='user', type='json')
    def viseducat_course_onboarding_panel(self):
        library = request.env['vm.media.type'].search([], limit=1, order="id desc")
        if library.library_onboarding_state == "closed":
            return {}

        return {
            'html': request.env.ref('viseducat_library.viseducat_library_onboarding_panel').render({
                'state': library.get_and_update_library_dashboard_onboarding_state()
            })
        }
