# -*- coding: utf-8 -*-
# from odoo import http


# class UmNotifikasiOnesignal(http.Controller):
#     @http.route('/um_notifikasi_onesignal/um_notifikasi_onesignal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/um_notifikasi_onesignal/um_notifikasi_onesignal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('um_notifikasi_onesignal.listing', {
#             'root': '/um_notifikasi_onesignal/um_notifikasi_onesignal',
#             'objects': http.request.env['um_notifikasi_onesignal.um_notifikasi_onesignal'].search([]),
#         })

#     @http.route('/um_notifikasi_onesignal/um_notifikasi_onesignal/objects/<model("um_notifikasi_onesignal.um_notifikasi_onesignal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('um_notifikasi_onesignal.object', {
#             'object': obj
#         })
