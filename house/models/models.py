

from odoo import models, fields

class MaterialRequest(models.Model):
    _name = 'material.request'
    _description = 'material.request'

    requester = fields.Char(string='Requester Name')
    material_name = fields.Char(string='Material Name')
    reason = fields.Text(string='Reason ')
    request_date = fields.Date(string='Request date')
    Necessity_level = fields.Selection([
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ], required=True , string='Necessity level')
    suggested_supplier = fields.Char(string='Suggested Supplier')

