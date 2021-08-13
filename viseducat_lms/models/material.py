from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re
from urllib.parse import urlparse
from math import modf


class VmMaterial(models.Model):
    _name = "vm.material"
    _inherit = "mail.thread"
    _description = "Material"

    name = fields.Char("Name", required=True)
    image_1920 = fields.Image("Image", max_width=512, max_height=512)
    user_id = fields.Many2one("res.users", string="User", readonly=True, required=True,
                              default=lambda self: self.env.user.id)
    website_url = fields.Char("Website URL", readonly=True)
    auto_publish = fields.Boolean("Auto Publish", default=False)
    material_type = fields.Selection(
        [('video', 'Video'), ('audio', 'Audio'), ('document', 'Document/PDF'), ('infographic', 'Image'),
         ('quiz', 'Quiz'), ('url', 'URL')], string='Material Type',
        required=True, default='video')
    video_type = fields.Selection(
        [('youtube', 'Youtube'), ('vimeo', 'Vimeo'), ('dartfish', 'DartFish'), ('fileupload', 'FileUpload'),
         ('quiz', 'Quiz'), ('url', 'URL')], string='Video Type',
        default='youtube')
    url = fields.Char("Document URL", )
    document_id = fields.Char("Document ID", )
    total_time = fields.Float("Total Time(HH:MM)", required=True)
    short_desc = fields.Text("Short Description")
    full_desc = fields.Html("Full Description")
    website_published = fields.Boolean(default=False)
    auto_publish_type = fields.Selection(
        [('wait_until', 'Wait Until'), ('wait_until_duration', 'Wait Until Duration')], string='Auto Publish Type',
    )
    wait_until_date = fields.Date("Wait Until")
    wait_until_duration = fields.Integer("Wait Until Duration")
    wait_until_duration_period = fields.Selection([
        ('minutes', 'Minutes'),
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('weeks', 'Weeks'),
        ('months', 'Months'),
        ('years', 'Years'),
    ])
    datas = fields.Binary("Content", help="Upload your file.")
    document_url = fields.Char("URL", )
    quiz_id = fields.Char("Quiz")
    active = fields.Boolean(default=True)

    # websitesi yapıldığından kodlanması gerekiyor!!!!!!!!!11
    def website_lms_publish_button(self):
        self.website_published = not self.website_published
        if self.website_published:
            print("publish edilecek")
        else:
            print("publish edilmeyecek")


    @api.onchange('url')
    def _validate_url(self):
        if self.url:
            regex = ("((http|https)://)(www.)?" +
                     "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                     "{2,256}\\.[a-z]" +
                     "{2,6}\\b([-a-zA-Z0-9@:%" +
                     "._\\+~#?&//=]*)")
            pattern = re.compile(regex)
            if not re.search(pattern, self.url):
                raise ValidationError(
                    _(f'Please enter valid URL: {self.url}'))

    @api.onchange('url')
    def _set_document_url(self):
        parsed_url = urlparse(self.url)
        if parsed_url.netloc == 'www.youtube.com':
            self.document_id = parsed_url.query[2:]

        elif parsed_url.netloc == 'vimeo.com':
            self.document_id = parsed_url.path[1:]
        else:
            #Burda hata var düzelt
            raise ValidationError(
                _("Couldn't fetch any document url"))



    def action_lms_onboarding_material_layout(self):
        course = self.env['vm.course'].search([('online_course', '=', True)], limit=1, order="id desc")
        course.sudo().set_onboarding_step_done('course_onboarding_lms_material_layout_state')
