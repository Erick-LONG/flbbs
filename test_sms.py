# encoding: utf-8
import requests


class MobSMS:
    def __init__(self, appkey):
        self.appkey = appkey
        self.verify_url = 'https://webapi.sms.mob.com/sms/verify'

    def verify_sms_code(self, zone, phone, code, debug=False):
        if debug:
            return 200

        data = {'appkey': self.appkey, 'phone': phone, 'zone': zone, 'code': code}
        req = requests.post(self.verify_url, data=data, verify=False)
        if req.status_code == 200:
            j = req.json()
            return j.get('status', 500)

        return 500


if __name__ == '__main__':
    mobsms = MobSMS('20bbe43ad9c1a')
    print('result----->'+ str(mobsms.verify_sms_code(86, 15313589743, '1234')))