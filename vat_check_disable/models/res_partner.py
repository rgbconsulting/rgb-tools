# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat_validation_fail = fields.Boolean(string='VAT Validation Fail', readonly=True, default=False)

    @api.multi
    def check_vat(self):
        company = self.env.user.company_id
        res = super(ResPartner, self).check_vat()
        if res:
            self.write({'vat_validation_fail': False})
            return res
        else:
            if company.disable_vat_check:
                self.write({'vat_validation_fail': True})
                return True
            return res

    @api.multi
    def _construct_constraint_msg(self):
        return super(ResPartner, self)._construct_constraint_msg()

    _constraints = [(check_vat, _construct_constraint_msg, ["vat"])]
