
from odoo.tests import common


class TestFeesCommon(common.SavepointCase):
    def setUp(self):
        super(TestFeesCommon, self).setUp()
        self.vm_student_fees = self.env['vm.student.fees.details']
        self.vm_student = self.env['vm.student']
        self.vm_fees_wizard = self.env['fees.detail.report.wizard']
        self.vm_fees_terms = self.env['vm.fees.terms']
