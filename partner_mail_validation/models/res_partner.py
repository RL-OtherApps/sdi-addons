###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import _, api, fields, models
from odoo.exceptions import UserError
from validate_email import validate_email


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def write(self, vals):
        res = super().write(vals)
        errors = []
        if 'email' in vals and not validate_email(vals.get('email')):
            errors.append('- Email has not a correct format')
        elif 'email' in vals and not validate_email(
                vals.get('email'), check_mx=True):
            errors.append('- The email domain has not SMTP server')
        elif 'email' in vals and not validate_email(
                vals.get('email'), verify=True):
            errors.append('- The email not really exists')
            raise UserError(_(
                'Sorry but the email does not have a correct format'))
        return res
