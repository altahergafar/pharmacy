# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class University(models.Model):
    _name = 'university.submission'
    # _description = 'university.university'

    parent_name = fields.Char(string='Parent Name', required=True)
    student_name = fields.Char(string='Student Name', required=True)
    # desc = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    request_Date = fields.Date(string="request Date", default=datetime.today())
    level = fields.Selection(string="Student Academic Level",  selection=[('bsc', 'Bachelor'), ('Msc', 'Masters'), ('Phd', 'Doctorate')], required=True)
    accepted = fields.Boolean()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
