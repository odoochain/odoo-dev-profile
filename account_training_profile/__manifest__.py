# © 2016-2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Account Training Profile',
    'version': '14.0.1.0.0',
    'category': 'Tools',
    'license': 'AGPL-3',
    'summary': 'Developer Profile',
    'description': """Add modules and set parameters that are usefull to give a training on accounting.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': [
        'dev_profile',
        'l10n_fr_account_vat_return_teledec',
        'account_asset_management',
        'sale_start_end_dates',
        'account_cutoff_start_end_dates',
        'account_cutoff_accrual_picking',
        'account_cutoff_accrual_subscription',
        ],
    'data': [
    ],
    'installable': True,
}
