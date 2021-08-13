# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Facility",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Facility',
    'license': 'LGPL-3',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['viseducat_core'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/facility_view.xml',
        'views/facility_line_view.xml',
        'menus/vm_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/facility_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
