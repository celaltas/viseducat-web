# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Timetable",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Timetable',
    'license': 'LGPL-3',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['viseducat_classroom'],

    # always loaded
    'data': [
        'security/vm_security.xml',
        'security/ir.model.access.csv',
        'views/timetable_view.xml',
        'views/timing_view.xml',
        'views/faculty_view.xml',
        'report/report_timetable_student_generate.xml',
        'report/report_timetable_teacher_generate.xml',
        'report/report_menu.xml',
        'wizard/generate_timetable_view.xml',
        'wizard/time_table_report.xml',
        #'wizard/session_confirmation.xml',
        'views/timetable_templates.xml',
        'views/timetable_analysis_view.xml',
        'views/batch_dashboard_view.xml',
        'menus/vm_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/timing_demo.xml',
        'demo/vm_timetable_demo.xml'
    ],
    'images': [
        'static/description/viseducat_timetable_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
