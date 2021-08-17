
from odoo.tests import common


class TestActivityCommon(common.SavepointCase):
    def setUp(self):
        super(TestActivityCommon, self).setUp()
        self.vm_activity_type = self.env['vm.activity.type']
        self.vm_activity = self.env['vm.activity']
        self.vm_student_migrate_wizard = self.env['student.migrate']
