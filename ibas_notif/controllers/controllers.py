# -*- coding: utf-8 -*-
# from odoo import http


# class IbasNotif(http.Controller):
#     @http.route('/ibas_notif/ibas_notif/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ibas_notif/ibas_notif/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ibas_notif.listing', {
#             'root': '/ibas_notif/ibas_notif',
#             'objects': http.request.env['ibas_notif.ibas_notif'].search([]),
#         })

#     @http.route('/ibas_notif/ibas_notif/objects/<model("ibas_notif.ibas_notif"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ibas_notif.object', {
#             'object': obj
#         })
