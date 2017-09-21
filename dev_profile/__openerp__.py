# -*- coding: utf-8 -*-
# Copyright (C) 2013-2017 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Developer Profile',
    'version': '0.1',
    'category': 'Tools',
    'license': 'AGPL-3',
    'summary': 'Developer Profile',
    'description': """Add modules and set parameters that are usefull to develop and test on Odoo.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': [
        # BASE
        'disable_openerp_online',
        'cron_run_manually',
        'base_import',
        'base_usability',
        #'mail_usability',
        'product_usability',
        'base_other_report_engines',
        'base_fix_display_address',
        'eradicate_quick_create',
        'document',
        # CRM
        'crm_usability',
        'sale_crm_usability',
        # ACCOUNT
        'account_cancel',
        'account_accountant',
        'account_journal_always_check_date',
        'account_financial_report_webkit',
        'account_financial_report_webkit_xls',
        'account_invoice_supplier_ref_unique',
        'account_move_line_no_default_search',
        'account_usability',
        'account_statement_completion_label_simple',
        'account_bank_statement_import_usability',
        'invoice_fiscal_position_update',
        'account_invoice_del_attachment_cancel',
        'l10n_fr_usability',
        # STOCK
        'stock_display_destination_move',
        'stock_usability',
        'stock_account_usability',
        'procurement_usability',
        # SALE
        'sale_usability_extension',
        'sale_stock_usability',
        # PURCHASE
        'purchase_usability_extension',
        'purchase_fiscal_position_update',
        # POS
        'pos_usability',
        # WEB
        'web_easy_switch_company',
        'web_sheet_full_width',
        'web_dialog_size',
        'web_translate_dialog',
        ],
    'data': [
        'profile.xml',
    ],
    'installable': True,
}
