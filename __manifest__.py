# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Hospital Management - apps.openerp.com""",

    'description': """
        Hospital Management
    """,

    'author': "Pradeepkumar",
    'website': "http://www.asdhospital.com",

    'category': 'Hodpital',
    'version': '0.1',

    'depends': ['base'],


    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
   # 'demo': [
    #    'demo/demo.xml',
    #],
}
