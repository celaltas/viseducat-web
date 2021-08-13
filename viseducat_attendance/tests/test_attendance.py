
from logging import info
import time
from .test_attendance_common import TestAttendanceCommon


class TestAttendanceRegister(TestAttendanceCommon):

    def setUp(self):
        super(TestAttendanceRegister, self).setUp()

    def test_case_attendance_register(self):
        register = self.vm_attendance_register.search([])
        for record in register:
            info('      Attendance Register : %s' % record.name)
            info('      Course : %s' % record.course_id.name)
            info('      Code : %s' % record.code)

class TestAttendanceSheet(TestAttendanceCommon):

    def setUp(self):
        super(TestAttendanceSheet, self).setUp()

    def test_case_attendance_sheet(self):
        sheet = self.vm_attendance_sheet.create({
            'name': 'AS',
            'attendance_date': time.strftime('%Y-%m-01'),
            'register_id':
                self.env.ref('viseducat_attendance.'
                             'vm_attendance_register_1').id
        })
        info('  Details Of Attendance Sheet:.....')
        for record in sheet:
            record.attendance_draft()
            record.attendance_start()
            record.attendance_done()
            record.attendance_cancel()
            record._compute_total_present()
            record._compute_total_absent()


class TestAttendanceLine(TestAttendanceCommon):

    def setUp(self):
        super(TestAttendanceLine, self).setUp()

    def test_case_attendance_line(self):
        line = self.vm_attendance_line.search([])
        info('  Details Of Attendance Lines:.....')
        for record in line:
            info('      Attendance Sheet : %s' % record.attendance_id.name)
            info('      Student : %s' % record.student_id.name)
            info('      Register : %s' % record.register_id.name)
            info('      Present : %s' % record.present)


class TestAttendanceImport(TestAttendanceCommon):

    def setUp(self):
        super(TestAttendanceImport, self).setUp()

    def test_case_wizard_attendance_import(self):
        wizard = self.vm_attendance_import.create({
            'course_id': self.env.ref('viseducat_core.vm_course_2').id,
            'batch_id': self.env.ref('viseducat_core.vm_batch_1').id,
            'student_ids': self.env.ref('viseducat_core.vm_student_1'),
        })
        wizard.confirm_student()


class TestAttendanceWizard(TestAttendanceCommon):

    def setUp(self):
        super(TestAttendanceWizard, self).setUp()

    def test_case_attendance_wizard(self):
        student = self.vm_attendance_wizard.create({
            'from_date': time.strftime('%Y-%m-01'),
            'to_date': time.strftime('%Y-%m-01')
        })
        student.print_report()
