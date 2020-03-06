###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def _notify_get_reply_to(
            self, default=None, records=None, company=None, doc_names=None):
        import wdb;wdb.set_trace()
        res = super()._notify_get_reply_to(
            self, default=None, records=None, company=None, doc_names=None)
        res = {account.id: self.env.user.id for account in self}
        return res
