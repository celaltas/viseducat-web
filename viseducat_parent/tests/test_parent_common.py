
from odoo.tests import common


class TestParentCommon(common.SavepointCase):
    def setUp(self):
        super(TestParentCommon, self).setUp()
        self.vm_parent = self.env['vm.parent']
        self.vm_student = self.env['vm.student']
        self.subject_registration = self.env['vm.subject.registration']
