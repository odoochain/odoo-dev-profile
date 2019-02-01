# -*- coding: utf-8 -*-
# © 2016-2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Developer Profile',
    'version': '12.0.1.0.0',
    'category': 'Tools',
    'license': 'AGPL-3',
    'summary': 'Developer Profile',
    'description': """Add modules and set parameters that are usefull to develop and test on Odoo.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': [
        # BASE
        'disable_odoo_online',
        'base_usability',
        #'mail_usability',
        'base_import',
        'document',
        'base_technical_features',
        'base_company_extension',
        #'web_export_view',
        #'web_no_bubble',
        #'eradicate_quick_create',
        #'web_dialog_size',
        #'web_translate_dialog',
        #'base_phone',
        # PRODUCT
        #'product_usability',
        # SALE
        'sale_crm',
        #'crm_usability',
        #'sale_usability',
        #'sale_stock_usability',
        #'sale_commercial_partner',
        # PURCHASE
        #'purchase_usability',
        #'purchase_commercial_partner',
        'purchase_stock',
        # PROCUREMENT
        #'procurement_usability',
        #'procurement_suggest',
        # STOCK
        'sale_stock',
        #'stock_usability',
        #'delivery_usability',
        # MRP
        'mrp',
        #'mrp_usability',
        # POS
        'point_of_sale',
        #'pos_usability',
        # ACCOUNT
        'account_cancel',
        'l10n_fr_fec',
        #'account_financial_report',
        'account_banking_sepa_credit_transfer',
        #'account_bank_statement_import_ofx',
        #'account_bank_statement_import_fr_cfonb',
        #'account_bank_statement_import_save_file',
        #'account_usability',
        #'account_bank_statement_import_usability',
        'account_fiscal_position_vat_check',
        #'account_invoice_fiscal_position_update',
        #'account_bank_statement_no_reconcile_guess',
        #'account_bank_reconciliation_summary_xlsx',
        ],
    'data': [
        'profile.xml',
    ],
    'demo': ['demo.xml'],
    'installable': True,
}
