from odoo.tests import common


class TestAttendanceCommon(common.SavepointCase):
    def setUp(self):
        super(TestAttendanceCommon, self).setUp()
        self.vm_attendance_register = self.env['vm.attendance.register']
        self.vm_attendance_sheet = self.env['vm.attendance.sheet']
        self.vm_attendance_line = self.env['vm.attendance.line']
        self.vm_attendance_import = self.env['vm.all.student']
        self.vm_attendance_wizard = self.env['student.attendance']
