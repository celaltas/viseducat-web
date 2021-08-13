# -*- coding: utf-8 -*-
{
    'name': "VisEduCat Library",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'category': 'Education',
    'summary': 'Manage Library',
    'license': 'LGPL-3',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['account', 'base_automation', 'viseducat_activity', 'viseducat_parent'],

    # always loaded
    'data': [

        'security/vm_security.xml',
        'security/ir.model.access.csv',
        'data/custom_paperformat.xml',
        'data/media_queue_sequence.xml',
        'data/action_rule_data.xml',
        'data/product_demo.xml',
        'report/report_media_barcode.xml',
        'report/report_library_card_barcode.xml',
        'report/report_student_library_card.xml',
        'report/report_menu.xml',
        'wizards/issue_media_view.xml',
        'wizards/return_media_view.xml',
        # 'wizards/reserve_media_view.xml',
        'views/media_view.xml',
        'views/media_unit_view.xml',
        'views/media_movement_view.xml',
        'views/media_purchase_view.xml',
        'views/media_queue_view.xml',
        'views/library_view.xml',
        'views/author_view.xml',
        'views/publisher_view.xml',
        'views/tag_view.xml',
        'views/media_type_view.xml',
        'views/student_view.xml',
        'views/faculty_view.xml',
        'views/library_media_analysis_view.xml',
        'views/library_media_unit_analysis_view.xml',
        'views/library_media_movement_analysis_view.xml',
        'views/library_media_queue_analysis_view.xml',
        'views/library_media_purchase_analysis_view.xml',
        'views/library_dashboard_view.xml',
        'views/library_onboarding_template.xml',
        'menus/vm_menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/media_type_demo.xml',
        'demo/res_users_demo.xml',
        'demo/tag_demo.xml',
        'demo/publisher_demo.xml',
        'demo/author_demo.xml',
        'demo/media_demo.xml',
        'demo/media_unit_demo.xml',
        'demo/media_queue_demo.xml',
        'demo/library_card_type_demo.xml',
        'demo/library_card_demo.xml',
        'demo/media_movement_demo.xml',
        'demo/media_purchase_demo.xml'
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
