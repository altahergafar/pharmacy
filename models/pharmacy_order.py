from odoo import models, fields, api
from datetime import datetime

class Pharmacy(models.Model):
    _name = 'pharmacy.order'
    _description = 'pharmacy.pharmacy'

    customer_treatments = fields.Text(string='Customer Treatments', required=True)
    date = fields.Date(string='Order_Date', default=datetime.today(), readonly=True)
    prescription = fields.Selection(string='Has a Prescription', selection=[('yes', 'Yes'), ('no', 'No')], required=True)
    suggested_pharmacy = fields.Text(string='Supplier')
    salesman = fields.Char(string='Salesman')


                           

# #
# #     @api.depends('value')
# #     def _value_pc(self):
# #         for record in self:
# #             record.value2 = float(record.value) / 100
