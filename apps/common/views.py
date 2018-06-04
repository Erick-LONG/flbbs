from flask import Blueprint,request
from exts import alidayu
from utils import restful
from utils.captcha import Captcha
from .forms import SMSCaptchaForm

common_bp = Blueprint('common',__name__,url_prefix='/c')


# @common_bp.route('/sms_captcha/')
# def sms_captcha():
#     #?telephone=xxx
#     telephone = request.args.get('telephone')
#     if not telephone:
#         return restful.params_error(message='请传入手机号码')
#
#     captcha = Captcha.gene_text(number=4)
#     if alidayu.send_sms(telephone,code=captcha):
#         return restful.success()
#     else:
#         return restful.params_error(message='短信验证码发送失败')

@common_bp.route('/sms_captcha/',methods=['POST'])
def sms_captcha():
    #telephone
    #timestamp
    #md5(ts +telephone+salt)
    form  = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        if alidayu.send_sms(telephone,code=captcha):
            return restful.success()
        else:
            return restful.params_error(message='短信验证码发送失败')
    else:
        return restful.params_error(message='参数错误')




