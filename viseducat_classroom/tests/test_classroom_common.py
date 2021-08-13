from odoo.tests import common


class TestClassroomCommon(common.SavepointCase):
    def setUp(self):
        super(TestClassroomCommon, self).setUp()
        self.vm_classroom = self.env['vm.classroom']
        self.vm_asset = self.env['vm.asset']
