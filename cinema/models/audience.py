# from odoo import models, fields, api
# from odoo.exceptions import ValidationError
#
#
# class Audience(models.Model):
#     _name = 'audience.audience'
#     _description = 'Display Audience Information'
#
#     a_name = fields.Char('Name', required=True, copy=True)
#     gender = fields.Selection([('m', 'Male'), ('f', 'Female')])
#     age = fields.Integer('Age')
#
#     @api.depends('reserve_fee', 'set_fee')
#     def compute_ticket_amount(self):
#         for rec in self:
#             if rec.set_fee and rec.reserve_fee:
#                 rec.ticket_amount = rec.reserve_fee + rec.set_fee
#             elif rec.set_fee:
#                 rec.ticket_amount = rec.set_fee
#             elif rec.reserve_fee:
#                 rec.ticket_amount = rec.reserve_fee
#             else:
#                 rec.ticket_amount = 0.0
#
#     reserve_fee = fields.Float('Reservation Fee')
#     set_fee = fields.Float('Set Fee')
#     ticket_amount = fields.Float('Ticket Amount', compute='compute_ticket_amount')
#
#     @api.model
#     def create(self, vals):
#         # overridden to automatically set audience age
#         if not vals.get('age'):
#             vals['age'] = 18
#         return super(Audience, self).create(vals)
