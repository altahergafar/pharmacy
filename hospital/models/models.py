#  # -*- coding: utf-8 -*-
#
from odoo import models, fields, api
#
#
class hospital(models.Model):
   _name = 'hospital.hospital'
   _description = 'hospital.hospital'
#
   first_name = fields.Char(string='First Name', required=True)
   middle_name = fields.Char(string='Middle Name', required=True)
   last_name = fields.Char(string='Last Name', required=True)
   patient_age = fields.Integer(string= 'Age')
   doctor_id = fields.Integer(string='Doctor Code', required=True)
   description= fields.Char(string='Description')
   priority = fields.Selection([('low','Low'),('medium','Medium'),('high','High')],Defualt='high', required=True)
   date = fields.Date(string='Date', default=fields.Date.today(),required=True)
# #     value2 = fields.Float(compute="_value_pc", store=True)
# #     description = fields.Text()
# #
# #     @api.depends('value')
# #     def _value_pc(self):
# #         for record in self:
# #             record.value2 = float(record.value) / 100
