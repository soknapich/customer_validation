# -*- coding: utf-8 -*-
{
    'name': "Customer Validation",

    'summary': """
        An app develop properly select customers to your company standards.""",

    'description': """
        An app develop properly select customers to your company standards.
        The app is focus on not overloading customers to which will results 
        to confusion on user end. 
        Validated customers will appear in our contacts 
        3 easy steps to validate a customer
        create 
        approve
        validate.
    """,

    'author': "Sokna Pich, Odoo Developer",
    'website': "http://www.somagroup.com.kh",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'SMG Group',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
