# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': """
        This module will add patient details  """,

    'description': """
       This module adding patient files and stoe
    """,

    'author': "iatl",
    'website': "http://www.iatl.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tool',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
       'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],'nstallable': True,
   # 'auto_install': True,
}
