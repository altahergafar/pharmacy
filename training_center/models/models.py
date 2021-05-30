# -*- coding: utf-8 -*-

from odoo import models, fields, api
# from odoo import DateTime

class training_center(models.Model):
   _name = 'training.center'
   _description = 'training_center.training_center'

   name = fields.Char(string='Course', required=True)
   candidates = fields.Text(string=' Candidates Names', required=True)
   hall = fields.Char(string='Hall Name' )
   start_date = fields.Datetime(string='Start Date',default=fields.Datetime.now)
   end_date = fields.Datetime(string ='End Date')
   price = fields.Float(string='Price', store=True,readonly=False)
   teacher = fields.Char(string='Teacher')
   certificate=fields.Boolean(string='Course has Certificate')
   announcement = fields.Selection([
        ('tv', 'TV'),
        ('radio', 'Radio'),
        ('social Media', 'Social Media')], string="Announcement On",required=True)

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
