# -*- coding: utf-8 -*-
# from odoo import http


# class Libarary(http.Controller):
#     @http.route('/libarary/libarary/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libarary/libarary/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('libarary.listing', {
#             'root': '/libarary/libarary',
#             'objects': http.request.env['libarary.libarary'].search([]),
#         })

#     @http.route('/libarary/libarary/objects/<model("libarary.libarary"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libarary.object', {
#             'object': obj
#         })
