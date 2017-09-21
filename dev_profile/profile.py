# -*- coding: utf-8 -*-
# (C) 2013-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.v7
    def init(self, cr):
        cr.execute("UPDATE account_journal SET update_posted=true")
        return True

    # Allow to cancel account moves
    update_posted = fields.Boolean(default=True)


class BaseLanguageExport(models.TransientModel):
    _inherit = 'base.language.export'

    # Default format for language files = format used by OpenERP modules
    format = fields.Selection(default='po')


class BaseLanguageInstall(models.TransientModel):
    _inherit = 'base.language.install'

    overwrite = fields.Boolean(default=True)
