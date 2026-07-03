{
    'name': 'Purchase Order Custom Column',
    'version': '19.0.1.0.0',
    'category': 'Purchases',
    'summary': 'Adds a custom column to Purchase Order Lines',
    'description': """
        This module adds a custom field/column to the Purchase Order Line view.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['base','purchase', 'account'],
    'data': [
        'views/purchase_order_view.xml',
        'views/account_move_view.xml',
        'report/purchase_order_report_inherit.xml',
        'report/purchase_qr_code_view.xml',

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
