from odoo import fields,models,api
import convert_numbers
# from deep_translator import GoogleTranslator
from uuid import uuid4
import qrcode
from odoo.exceptions import UserError

import base64
import logging

from lxml import etree

logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'


    def invoice_date_time_test(self):
        # return self.invoice_date_time.split(' ')[0]
        # return self.invoice_date_time.split(' ')[0]
        return self.invoice_date_time

