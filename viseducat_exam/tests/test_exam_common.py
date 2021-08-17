
from odoo.tests import common


class TestExamCommon(common.SavepointCase):
    def setUp(self):
        super(TestExamCommon, self).setUp()
        self.vm_exam = self.env['vm.exam']
        self.vm_exam_attendees = self.env['vm.exam.attendees']
        self.vm_exam_room = self.env['vm.exam.room']
        self.vm_exam_session = self.env['vm.exam.session']
        self.vm_exam_type = self.env['vm.exam.type']
        self.vm_grade_configuration = self.env['vm.grade.configuration']
        self.vm_marksheet_line = self.env['vm.marksheet.line']
        self.vm_marksheet_register = self.env['vm.marksheet.register']
        self.vm_res_partner = self.env['res.partner']
        self.vm_result_line = self.env['vm.result.line']
        self.vm_result_template = self.env['vm.result.template']
        self.vm_held_exam = self.env['vm.held.exam']
        self.vm_room_distribution = self.env['vm.room.distribution']
        self.student_hall_ticket = self.env['student.hall.ticket']
