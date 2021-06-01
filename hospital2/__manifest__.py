# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Hospital Erp System Management",

    'description': """
      
    """,

    'author': "Huzaifa",
    'website': "huz.dark1@gmail.com",
    'category': 'Health',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hospital.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
