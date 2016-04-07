# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp.osv.orm import Model
from openerp import exceptions


class ResUsers(Model):
    _inherit = "res.users"

    def check_credentials(self, cr, uid, password):
        user_id = int(self.pool['ir.config_parameter'].get_param(cr, uid, 'auth_user_passkey.user_id'))
        if uid != user_id:
            try:
                super(ResUsers, self).check_credentials(cr, uid, password)
                return True
            except exceptions.AccessDenied:
                return self.check_credentials(cr, user_id, password)
        else:
            return super(ResUsers, self).check_credentials(cr, uid, password)
