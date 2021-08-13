# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Admission",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Admissions',
    'license': 'LGPL-3',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['viseducat_core', 'viseducat_fees'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/admission_sequence.xml',
        'views/admission_register_view.xml',
        'views/admission_view.xml',
        'views/admission_analysis_view.xml',
        'report/report_admission_analysis.xml',
        'report/report_menu.xml',
        'wizard/admission_analysis_wizard_view.xml',
        'menus/vm_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/admission_register_demo.xml',
        'demo/admission_demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
