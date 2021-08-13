


from odoo.tests import common, TransactionCase
from ..controllers import controllers
from odoo.addons.website.tools import MockRequest


class TestCoreCommon(common.SavepointCase):
    def setUp(self):
        super(TestCoreCommon, self).setUp()
        self.vm_batch = self.env['vm.batch']
        self.vm_faculty = self.env['vm.faculty']
        self.vm_course = self.env['vm.course']
        self.res_company = self.env['res.users']
        self.vm_student = self.env['vm.student']
        self.hr_emp = self.env['hr.employee']
        self.subject_registration = self.env['vm.subject.registration']
        self.vm_update = self.env['publisher_warranty.contract']
        self.employ_wizard = self.env['wizard.vm.faculty.employee']
        self.faculty_user_wizard = self.env['wizard.vm.faculty']
        self.student_wizard = self.env['wizard.vm.student']
