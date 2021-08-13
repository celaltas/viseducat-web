# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Exam",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Exam',
    'license': 'LGPL-3',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['viseducat_classroom'],

    # always loaded
    'data': [

        'security/vm_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/exam_attendees_view.xml',
        'views/exam_room_view.xml',
        'views/exam_session_view.xml',
        'views/exam_type_view.xml',
        'wizard/room_distribution_view.xml',
        'wizard/held_exam_view.xml',
        'views/exam_view.xml',
        'views/marksheet_line_view.xml',
        'views/marksheet_register_view.xml',
        'views/grade_configuration_view.xml',
        'views/result_line_view.xml',
        'views/result_template_view.xml',
        'report/report_ticket.xml',
        'report/student_marksheet.xml',
        'report/report_menu.xml',
        'wizard/student_hall_tickets_wizard_view.xml',
        'views/exam_dashboard_view.xml',
        'menus/vm_menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/exam_room_demo.xml',
        'demo/exam_type_demo.xml',
        'demo/exam_session_demo.xml',
        'demo/exam_demo.xml',
        'demo/exam_attendees_demo.xml',
        'demo/grade_configuration_demo.xml',
        'demo/result_template_demo.xml',
        'demo/marksheet_register_demo.xml',
        'demo/marksheet_line_demo.xml',
        'demo/result_line_demo.xml',

    ],
    'images': [
        'static/description/viseducat_exam_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
