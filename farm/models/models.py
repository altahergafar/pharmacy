# -*- coding: utf-8 -*-

from odoo import models, fields


class Farm(models.Model):
    _name = 'farm.farm'
    _description = 'farm.farm'

    Requester = fields.Char(string="Requester", required=True)
    material_name = fields.Char(string="Material", required=True)
    project = fields.Char(string="Project")
    request_date = fields.Date('Date', required=False, readonly=True, select=True
                               , default=lambda self: fields.datetime.now())
    suggested_supplier = fields.Char(string="Supplier")
    necessary_level = fields.Selection([('high', 'High'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High'),
                                        ], string="Level", default='low', required=True, )

