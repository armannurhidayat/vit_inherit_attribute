# -*- coding: utf-8 -*-
{
    'name': "inherit attribute mobile",

    'summary': """
        Inherit attribute required
    """,

    'description': """
        Inherit attribute required res.partner
    """,

    'author': "Arman Nur Hidayat",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}