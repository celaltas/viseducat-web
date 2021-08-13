# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Assignment",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Admissions',
    'license': 'LGPL-3',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base_automation', 'viseducat_core'],

    # always loaded
    'data': [
        # 'security/vm_security.xml',
        'security/ir.model.access.csv',
        'security/vm_security.xml',
        'views/assignment_view.xml',
        'views/assignment_type_view.xml',
        'views/assignment_sub_line_view.xml',
        'views/assignment_analysis_view.xml',
        'views/assignment_submission_analysis_view.xml',
        'views/student_view.xml',
        'data/action_rule_data.xml',
        'menus/vm_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/assignment_type_demo.xml',
        'demo/assignment_demo.xml',
        'demo/assignment_sub_line_demo.xml'
    ],
    'images': [
        # 'static/description/viseducat_assignment_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
