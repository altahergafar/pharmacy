# -*- coding: utf-8 -*-
from odoo import models, fields
from datetime import datetime


class CallCenter(models.Model):
    _name = 'ticket.ticket'
    _description = "Call Center"

    name = fields.Char(string='Requester', required=True)
    email = fields.Char(string='Email', required=True)        
    phone = fields.Char(string='Phone', required=True)       
    subject = fields.Char(string='Subject', required=True)
    Description = fields.Text(string='Description')
    date = fields.Date(string='Request date', readonly=True, default=fields.Date.today())
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in-progress', 'In Progress'),
        ('close', 'Close'),], string="Status", required=True, default='draft')


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
# defualt= lambda self:fields.datetime.now() readonly=True, context_today
