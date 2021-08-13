# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Core",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Students, Faculties and Education Institute',
    'license': 'LGPL-3',
    'version': '13.0',


    # any module necessary for this one to work correctly
    'depends': ['board', 'hr', 'web', 'website'],

    # always loaded
    'data': [
        'security/vm_security.xml',
        'security/ir.model.access.csv',
        'report/report_menu.xml',
        'report/report_student_bonafide.xml',
        'report/report_student_idcard.xml',
        'wizard/faculty_create_employee_wizard_view.xml',
        'wizard/faculty_create_user_wizard_view.xml',
        'wizard/students_create_user_wizard_view.xml',
        'views/department_view.xml',
        'views/res_company_view.xml',
        'views/student_view.xml',
        'views/hr_view.xml',
        'views/category_view.xml',
        'views/course_view.xml',
        'views/batch_view.xml',
        'views/subject_view.xml',
        'views/faculty_view.xml',
        # 'views/website_assets.xml',
        'views/subject_registration_view.xml',
        # 'views/res_config_setting_view.xml',
        'views/student_portal_view.xml',
        'views/student_course_view.xml',
        'views/course_dashboard_view.xml',
        'views/batch_dashboard_view.xml',
        'views/course_onboarding_template.xml',
        'menu/viseducat_core_menu.xml',
        'menu/faculty_menu.xml',
        'menu/student_menu.xml',
        'menu/course_menu.xml',
        'menu/batch_menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/homepage_template.xml',
        'demo/department_demo.xml',
        'demo/base_demo.xml',
        'demo/res_partner_demo.xml',
        'demo/res_users_demo.xml',
        'demo/subject_demo.xml',
        'demo/course_demo.xml',
        'demo/batch_demo.xml',
        'demo/student_demo.xml',
        'demo/student_course_demo.xml',
        'demo/faculty_demo.xml',
        'demo/res_condig_fav_icon.xml',

    ],
    'css': [
        # 'static/src/scss/base.scss'
    ],
    'qweb': [
        # 'static/src/xml/base.xml',
        # 'static/src/xml/dashboard_ext_viseducat.xml'
    ],
    'js': [],
    'images': [
        # 'static/description/viseducat_core_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
