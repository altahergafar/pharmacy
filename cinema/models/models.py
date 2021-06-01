# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class Cinema(models.Model):
    _name = 'cinema.show'
    _description = 'An Erp System for Cinema'

    show_hall = fields.Char('Show Hall', required=True, copy=True)
    nums_sets = fields.Integer('Number of Sets')
    reserved_seat_no = fields.Integer('Reserved Seats Number')
    halls_supervisor = fields.Char('Supervisor')


class Movie(models.Model):
    _name = 'movie.show'

    movie_name = fields.Char('Movie Name', required=True)
    movie_duration = fields.Float('Movie Duration')
    movie_date = fields.Date('Movie Date')
    tickets_sold = fields.Boolean('Tickets are Sold out')
    description = fields.Text('Description')
    sequence = fields.Char(readonly=True, copy=False)

    @api.onchange('tickets_sold', 'movie_name')
    def _onchange_ticket_sold(self):
        if self.tickets_sold:
            self.description = 'Tickets are sold out'

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('movie.show')

        res = super(Movie, self).create(vals)
        return res
