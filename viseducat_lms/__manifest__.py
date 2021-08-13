# -*- coding: utf-8 -*-
{
    'name': "viseducat_lms",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','viseducat_core', 'sale', 'event', 'website_event'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/course_category_view.xml',
        'views/course_section_view.xml',
        'views/course_section_material_line_view.xml',
        'views/material_view.xml',
        'views/course_view.xml',
        'views/enrollment_view.xml',
        'views/course_dashboard_view.xml',
        'views/course_lms_onboarding_template.xml',
        'menus/menus.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
