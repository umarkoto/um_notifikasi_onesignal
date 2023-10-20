from odoo import api, models

class StpdDinasInherit(models.Model):
    _inherit = 'stpd.dinas'

    @api.model
    def create(self, vals):
        record = super(StpdDinasInherit, self).create(vals)

        # Kirim notifikasi dengan OneSignal setelah record berhasil dibuat
        message = "Pengajuan dinas baru dengan Nomor: {} telah berhasil dibuat.".format(record.name)
        self.env['onesignal.notification'].send_notification(message)

        return record
