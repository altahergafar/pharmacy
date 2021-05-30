# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HallReservationRequest(models.Model):
     _name = 'hall.reservation.request'
     _description = 'hotel_hotel'

     name = fields.Char(string="name", required=True)
     hall_code = fields.Integer(string="hall code", required=True)
     description = fields.Text(string="description")
     date = fields.Integer(string="date", readonly=True)
     hours = fields.Float(string="hours")
     availableTime = fields.datetime(string="available_time")
