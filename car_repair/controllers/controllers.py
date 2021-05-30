# -*- coding: utf-8 -*-
# from odoo import http


# class CarRepair(http.Controller):
#     @http.route('/car_repair/car_repair/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_repair/car_repair/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_repair.listing', {
#             'root': '/car_repair/car_repair',
#             'objects': http.request.env['car_repair.car_repair'].search([]),
#         })

#     @http.route('/car_repair/car_repair/objects/<model("car_repair.car_repair"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_repair.object', {
#             'object': obj
#         })
