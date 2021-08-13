
from odoo.tests import common


class TestTimetableCommon(common.SavepointCase):
    def setUp(self):
        super(TestTimetableCommon, self).setUp()
        self.vm_faculty = self.env['vm.faculty']
        self.vm_session = self.env['vm.session']
        self.vm_timing = self.env['vm.timing']
        self.generate_timetable = self.env['generate.time.table']
        self.wizard_session = self.env['gen.time.table.line']
        self.timetable_report = self.env['time.table.report']
