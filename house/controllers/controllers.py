# -*- coding: utf-8 -*-
# from odoo import http


# class House(http.Controller):
#     @http.route('/house/house/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/house/house/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('house.listing', {
#             'root': '/house/house',
#             'objects': http.request.env['house.house'].search([]),
#         })

#     @http.route('/house/house/objects/<model("house.house"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('house.object', {
#             'object': obj
#         })
