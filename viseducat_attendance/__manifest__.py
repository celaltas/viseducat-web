# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Attendance",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Attendances',
    'license': 'LGPL-3',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['viseducat_timetable'],

    # always loaded
    'data': [
        'security/vm_security.xml',
        'security/ir.model.access.csv',
        'data/attendance_sheet_sequence.xml',
        'wizards/attendance_import_view.xml',
        'wizards/student_attendance_wizard_view.xml',
        'views/attendance_register_view.xml',
        'views/attendance_sheet_view.xml',
        'views/attendance_sheet_analysis_view.xml',
        'views/attendance_line_analysis_view.xml',
        'views/attendance_line_view.xml',
        'views/attendance_type_view.xml',
        'views/attendance_session_view.xml',
        'views/attendance_onboarding_template.xml',
        'views/batch_dashboard_view.xml',
        'report/student_attendance_report.xml',
        'report/report_menu.xml',
        'menus/vm_menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/attendance_register_demo.xml',
        'demo/attendance_sheet_demo.xml',
        'demo/attendance_line_demo.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
