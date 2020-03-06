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
        import wdb;wdb.set_trace()
        if 'email' in vals and not validate_email(vals['email']):
            errors.append('- Email has not a correct format')
        elif 'email' in vals and not validate_email(
                vals['email'], check_mx=True):
            errors.append('- The email domain has not SMTP server')
        elif 'email' in vals and not validate_email(
                vals['email'], verify=True):
            errors.append('- The email not really exists')
        if errors:
            validations = '\n'.join(errors)
            raise UserError(_(
                'Error in the email field: \n%s' % validations))
        return res
