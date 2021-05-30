# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CarRepair(models.Model):
   _name = 'car.repair'
   _description = 'car_repair manager module'

   name = fields.Char(string="Requester", required=True)
   car = fields.Char(string="Car_Name" , required=True)
   person= fields.Char(string="Responsible")
   problem = fields.Text(string="issue", required=True)
   current_date= fields.Date(string="Date", default=fields.Date.today, readonly=True)
   need=fields.Char(string="spare_part")

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
