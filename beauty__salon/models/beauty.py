# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class beautysalon(models.Model):
    _name = 'beauty__salon.beauty__salon'
    _description = 'beauty__salon.beauty__salon'

    name = fields.Char(string='Name',required=True)
    Service = fields.Char(string='Service', required=True)
    ExpertName = fields.Char(string='Expert')
    Request_date= fields.Date(string="Date", default=fields.Date.today, reaonly=True)
    Duration = fields.Float(string="Duration")
    Cost = fields.Float(string="Cost")
#     description = fields.Text(string='description ')

     #@api.depends('value')
     #def _value_pc(self):
        # for record in self:
            # record.value2 = float(record.value) / 100
