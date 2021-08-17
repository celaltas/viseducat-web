

from odoo.tests import common


class TestAssignmentCommon(common.SavepointCase):
    def setUp(self):
        super(TestAssignmentCommon, self).setUp()
        self.vm_assignment = self.env['vm.assignment']
        self.vm_assignment_subline = self.env['vm.assignment.sub.line']
