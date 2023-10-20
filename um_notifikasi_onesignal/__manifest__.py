# -*- coding: utf-8 -*-
{
    'name': "One Signal Notifikasi Connector",

    'summary': """
        OneSignal connector""",

    'description': """
        OneSignal connector
    """,

    'currency': 'EUR',
    'price': 30,

    'author': "Umar",
    'website': "https://idkotoo.com",
    'maintainer': 'idkotoo',
    'images': ['static/description/main1.png', 'static/description/main2.png'],
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '16.0.1.0.1',
    'images': ['static/description/banner.gif'],
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/assets.xml',
        'views/onesignal_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
