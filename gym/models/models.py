# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Request(models.Model):
    _name = 'registration.request'
    _description = 'registration.request'
    Requester = fields.Char('name', required=True)
    Program_Name = fields.Char('program', required=True)
    Coach_Name = fields.Char('coach')
    Request_Date = fields.Date('date', readonly=False, default=fields.Date.today())
    Date_From = fields.Date('date_From', required=True)
    Date_To = fields.Date('date_To')

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
