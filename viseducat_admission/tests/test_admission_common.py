
from odoo.tests import common


class TestAdmissionCommon(common.SavepointCase):
    def setUp(self):
        super(TestAdmissionCommon, self).setUp()
        self.vm_register = self.env['vm.admission.register']
        self.vm_admission = self.env['vm.admission']
        self.wizard_admission = self.env['admission.analysis']
