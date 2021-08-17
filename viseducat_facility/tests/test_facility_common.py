
from odoo.tests import common


class TestFacilityCommon(common.SavepointCase):
    def setUp(self):
        super(TestFacilityCommon, self).setUp()
        self.vm_facility_line = self.env['vm.facility.line']
