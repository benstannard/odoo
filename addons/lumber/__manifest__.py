{
        'name': 'Lumber',
        'version': '0.1',
        'license': 'AGPL-3',
        'depends': ['base'],
        'author': 'Ben Stannard',
        'website': 'https://github.com/benstannard',
        'category': 'Services',
        'summary': 'Guide for lumber sales',
        'description': """
        Test module using lumber to learn about Odoo architecture
        """,
        'data': [
            'security/ir.model.access.csv',
            'views/lumber_menu.xml',
            ],
        'application': True,
        'installable': True,
        'auto_install': False,
}
