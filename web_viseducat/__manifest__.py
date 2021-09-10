{
    'name': "Web VisEduCat",
    'author': "VisMarin Bilisim",
    'website': "https://www.vismarin.com/en/",
    'summary': 'VisEduCat Website',
    'license': 'LGPL-3',
    'version': '13.0',

    'data': [
        'views/assets.xml',
        'views/snippets/slider.xml',
        'views/snippets/about-us.xml',
        'views/snippets/ourcourse.xml',
        'views/snippets/achievement.xml',
        'views/snippets/teacher.xml',
        'views/snippets/event.xml',
        'views/snippets/newsfeed.xml',
        'views/snippets/footer.xml',
        'views/image_library.xml',
        'views/courses_view.xml',
        'views/course_details_view.xml',
        'views/registration.xml',
        'views/menu.xml',
        'views/payment.xml',
        'views/cart.xml',
        'views/confirmation.xml',
        'views/confirm_order.xml'
        

    ],
    'qweb': [
        "static/src/xml/base_inherit.xml",
    ],
    'demo': [
        'data/homepage_demo.xml',
        'data/footer_template.xml',
    ],
    'images': [
        'static/description/web_openeducat_banner.jpg',
    ],
    'depends': [
        'website',
    ],
    'application': True,
}
