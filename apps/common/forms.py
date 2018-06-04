from wtforms import StringField
from apps.forms import BaseForm
from wtforms.validators import regexp,InputRequired
import hashlib

class SMSCaptchaForm(BaseForm):
    salt = 'fsfkjsfbjkffjbkjfdfkdfbn'
    telephone = StringField(validators=[regexp(r'1[345789]\d{9}')])
    timestamp = StringField(validators=[regexp(r'\d{13}')])
    sign = StringField(validators=[InputRequired()])

    def validate(self):
        result = super(SMSCaptchaForm,self).validate()
        if not result:
            return False
        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign  = self.sign.data

        #md5必须传入byte类型
        sign2 = hashlib.md5((timestamp+telephone+self.salt).encode('utf-8')).hexdigest()
        if sign == sign2:
            return True
        else:
            return False
