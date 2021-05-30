# -*- coding: utf-8 -*-
# from odoo import http


# class BeautySalon(http.Controller):
#     @http.route('/beauty__salon/beauty__salon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/beauty__salon/beauty__salon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('beauty__salon.listing', {
#             'root': '/beauty__salon/beauty__salon',
#             'objects': http.request.env['beauty__salon.beauty__salon'].search([]),
#         })

#     @http.route('/beauty__salon/beauty__salon/objects/<model("beauty__salon.beauty__salon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('beauty__salon.object', {
#             'object': obj
#         })
