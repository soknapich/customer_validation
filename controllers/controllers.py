# -*- coding: utf-8 -*-
from odoo import http

# class CustomerValidation(http.Controller):
#     @http.route('/customer_validation/customer_validation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_validation/customer_validation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_validation.listing', {
#             'root': '/customer_validation/customer_validation',
#             'objects': http.request.env['customer_validation.customer_validation'].search([]),
#         })

#     @http.route('/customer_validation/customer_validation/objects/<model("customer_validation.customer_validation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_validation.object', {
#             'object': obj
#         })