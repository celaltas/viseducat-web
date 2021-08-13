# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Parent",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Parent',
    'license': 'LGPL-3',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['viseducat_core'],

    # always loaded
    'data': [
        'security/vm_security.xml',
        'security/ir.model.access.csv',
        'data/parent_user_data.xml',
        'views/parent_view.xml',
        'views/parent_relationship_view.xml',
        'menus/vm_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/res_partner_demo.xml',
        'demo/res_users_demo.xml',
        'demo/parent_relationship_demo.xml',
        'demo/parent_demo.xml',
    ],
    'images': [
        'static/description/viseducat_parent_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
