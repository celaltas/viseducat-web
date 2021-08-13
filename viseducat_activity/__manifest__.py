# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Activity",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'depends': ['viseducat_core'],
    'summary': 'Manage Activities',
    'license': 'LGPL-3',
    'version': '13.0',

    # always loaded
    'data': [

        'security/vm_security.xml',
        'security/ir.model.access.csv',
        'data/activity_type_data.xml',
        'wizard/student_migrate_wizard_view.xml',
        'views/activity_view.xml',
        'views/activity_type_view.xml',
        'views/student_view.xml',
        'menus/vm_menu.xml'


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/activity_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
