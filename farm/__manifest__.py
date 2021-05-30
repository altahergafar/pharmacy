# -*- coding: utf-8 -*-
{
    'name': "farm",
    'summary': """This is farm system v1.0""",
    'description': """ERP system for farm management""",
    'author': "mohammed azez",
    'website': "http://www.iatl-sof.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': -1,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_account_post_init',
}
