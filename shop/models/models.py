# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

class shop(models.Model):
    _name = 'material.request'
    _description = 'material.request'

    requester = fields.Char(string="Requester", required=True)
    material_name = fields.Char(string="Material Name", required=True)
    reason = fields.Text(string="Reason")
    request_date = fields.Date(string="Request Date", default=datetime.today(), readonly=True)
    necessity_level = fields.Selection([('High','high'), ('Medium','medium'),('Low','low')], required=True)
    supplier = fields.Char(string="Supplier")