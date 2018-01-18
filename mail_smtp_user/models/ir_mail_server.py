# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import models, fields, api
from openerp.addons.base.ir.ir_mail_server import extract_rfc2822_addresses


class IrMailServer(models.Model):
    _inherit = "ir.mail_server"

    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False):
        # Find server for sender email
        from_rfc2822 = extract_rfc2822_addresses(message['From'])[-1]
        mail_server = self.search([('smtp_user', '=', from_rfc2822)], limit=1)
        if mail_server:
            mail_server_id = mail_server.id
        return super(IrMailServer, self).send_email(message=message, mail_server_id=mail_server_id,
                                                    smtp_server=smtp_server, smtp_port=smtp_port,
                                                    smtp_user=smtp_user, smtp_password=smtp_password,
                                                    smtp_encryption=smtp_encryption, smtp_debug=smtp_debug)
