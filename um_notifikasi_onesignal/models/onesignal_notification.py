from odoo import api, models, fields
import requests
import json
from odoo.exceptions import UserError


class OneSignalNotification(models.Model):
    _name = 'onesignal.notification'

    authorization_key = fields.Char('Authorization Key')
    app_id = fields.Char('App ID')

    @api.model
    def send_notification(self, message):
        config = self.env['onesignal.notification'].search([], limit=1)
        if not config:
            raise UserError("Please configure the OneSignal settings first!")

        headers = {
            "Content-Type": "application/json; charset=utf-8",
            # "Authorization": "Basic ZjgwMTQ1ZjktOTM5NC00NGMwLTg0OTQtMTZkMjAwY2JkZGRm"
            "Authorization": "Basic %s" % config.authorization_key  # Use value from the found record
        }

        payload = {
            # "app_id": "ad8fa019-c946-41c2-941b-bf0c0615081d",
            "app_id": config.app_id,  # Use value from the found record
            "included_segments": ["All"],
            "contents": {"en": message}
        }

        response = requests.post("https://onesignal.com/api/v1/notifications", headers=headers,
                                 data=json.dumps(payload))
        print(response.status_code)
        print(response.json())
        if response.status_code == 200:
            return True
        else:
            self.env.cr.rollback()  # Rollback transaction if there's a failure in sending notification
            raise UserError("Failed to send OneSignal Notification! Response: %s" % response.text)

        return False
