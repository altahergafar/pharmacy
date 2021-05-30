# -*- coding: utf-8 -*-
# from odoo import http


# class Farm(http.Controller):
#     @http.route('/farm/farm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/farm/farm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('farm.listing', {
#             'root': '/farm/farm',
#             'objects': http.request.env['farm.farm'].search([]),
#         })

#     @http.route('/farm/farm/objects/<model("farm.farm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('farm.object', {
#             'object': obj
#         })
