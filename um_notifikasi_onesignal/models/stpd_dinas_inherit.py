from odoo import api, models

# class StpdDinasInherit(models.Model):
#     _inherit = 'stpd.dinas'

#     @api.model
#     def create(self, vals):
#         record = super(StpdDinasInherit, self).create(vals)

#         # Kirim notifikasi dengan OneSignal setelah record berhasil dibuat
#         message = "Pengajuan dinas baru dengan Nomor: {} telah berhasil dibuat.".format(record.name)
#         self.env['onesignal.notification'].send_notification(message)

#         return record

class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def create(self, vals):
        record = super(HrEmployeeInherit, self).create(vals)

        # Send notification with OneSignal after employee record is successfully created
        message = "A new employee named {} has been successfully added.".format(record.name)
        self.env['onesignal.notification'].send_notification(message)

        return record
