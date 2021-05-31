# -*- coding: utf-8 -*-


from odoo import models, fields, api
from isodate.isostrf import DATE_BAS_WEEK, DATE_BAS_WEEK_COMPLETE
from datetime import datetime


class Cinema(models.Model):
    _name = 'cinema.cinema'
    _description = 'An Erp System for Cinema'

    show_hall = fields.Char('Show Hall', required=True, copy=True)
    nums_sets = fields.Integer('Number of Sets')
    reserved_seat_no = fields.Integer('Reserved Seats Number')
    halls_supervisor = fields.Char('Supervisor')
    movie_duration = fields.Float('Movie Duration')
    tickets_sold = fields.Boolean('Tickets are Sold out')


class Film(models.Model):
    _name = 'film.film'
    _description = 'Film and Display Information'

    f_name = fields.Char('Film Name', required=True, copy=True)
    movie_date = fields.Date('Movie Date')
