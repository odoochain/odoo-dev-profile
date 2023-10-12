# © 2016-2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Developer Profile',
    'version': '16.0.1.0.0',
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
        'remove_odoo_enterprise',
        'base_usability',
        'web_dark_mode',
        'mail_usability',
        'base_technical_features',
        'base_company_extension',
        'partner_disable_gravatar',
        'partner_firstname',
        # Don't depend on partner_bank_acc_type_constraint
        # because it blocks the demo data of account_statement_import_file
        # and probably other modules
        #'partner_bank_acc_type_constraint',
        'auth_admin_passkey',
        'web_no_bubble',
        'web_responsive',
        'eradicate_quick_create',
        'web_dialog_size',
        #'web_translate_dialog',
        'web_dark_mode',
        'phone_validation',
        #'base_phone',
        # PRODUCT
        'product_usability',
        # SALE
        'sale_crm',
        'sale_management',
        'crm_usability',
        'sale_usability',
        'sale_stock_usability',
        'sale_commercial_partner',
        # PURCHASE
        'purchase',
        'purchase_usability',
        'purchase_commercial_partner',
        'purchase_stock_usability',
        # PROCUREMENT
        # STOCK
        'sale_stock',
        'stock_usability',
 #       'stock_account_usability',
        'delivery_usability',
        # MRP
        'mrp_usability',
        # POS
        'point_of_sale',
        'pos_usability',
        # ACCOUNT
        'account',
        'account_usability',
        'account_usability_akretion',
         'account_move_name_sequence',
        'currency_rate_update',
        'date_range',
        'date_range_account',
 #       'account_partner_required',
        'l10n_fr_fec_oca',
 #       'account_fiscal_year',
         'account_financial_report',
        'account_banking_sepa_credit_transfer',
        'account_payment_sale',
         'account_check_deposit',
         'account_cash_deposit',
         'account_move_csv_import',
        'account_statement_import_ofx',
        'account_statement_import_fr_cfonb',
        'account_reconcile_oca',
        'account_fiscal_position_vat_check',
        'account_lock_date_update',
        'l10n_fr_das2',
        'l10n_fr_mis_reports',
        'account_balance_ebp_csv_export',
         'account_invoice_transmit_method',
        'account_invoice_overdue_reminder',
        'l10n_fr_intrastat_product',
        'l10n_fr_intrastat_service',
        'l10n_fr_siret',
        'l10n_fr_siret_lookup',
        'l10n_fr_account_invoice_facturx',
        'account_invoice_import_facturx',
        'account_invoice_import_simple_pdf',
        'account_statement_completion_label_simple_sale',
        'account_cutoff_start_end_dates',
        'l10n_fr_account_vat_return_teledec',
        #'account_invoice_fiscal_position_update',
        ],
    'data': [
        'profile.xml',
    ],
#    'demo': ['demo.xml'],
    'installable': True,
}
