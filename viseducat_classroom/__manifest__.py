# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Classroom",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Classroom',
    'license': 'LGPL-3',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['viseducat_core', 'viseducat_facility', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/classroom_view.xml',
        'menus/vm_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/classroom_demo.xml',
        'demo/facility_line_demo.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
