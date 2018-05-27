from flask import Blueprint, views, render_template, request, session, redirect, url_for, g,jsonify

from exts import db,mail
from .decorators import login_required

from .forms import LoginForm,ResetpwdForm
from .models import CmsUser
import config
from flask_mail import Message
from utils import restful

cms_bp = Blueprint('cms',__name__,url_prefix='/cms')


@cms_bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


@cms_bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))


@cms_bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')

@cms_bp.route('/email/')
def send_mail():
    message = Message('邮件发送',recipients=['834424581@qq.com'],body='测试')
    mail.send(message)
    return 'success'

class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/cms_login.html',message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CmsUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='邮箱或验证码错误')
        else:
            #print(form.errors)
            message = form.errors.popitem()[1][0]
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                # {"code":200,message=""}
                # return jsonify({"code":200,"message":""})
                return restful.success()
            else:
                return restful.params_error("旧密码错误！")
        else:
            return restful.params_error(form.get_error())


class ResetEmailView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetemail.html')
    def post(self):
        pass

cms_bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))
cms_bp.add_url_rule('/resetpwd/',view_func=ResetPwdView.as_view('resetpwd'))
cms_bp.add_url_rule('/resetemail/',view_func=ResetEmailView.as_view('resetemail'))