from flask import Blueprint, views, render_template, request, session, redirect, url_for, g,jsonify
import string,random
from exts import db,mail
from .decorators import login_required,permission_required

from .forms import LoginForm,ResetpwdForm,ResetEmailForm
from .models import CmsUser,CMSPersmmission
import config
from flask_mail import Message
from utils import restful,zlcache

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

@cms_bp.route('/email_captcha/')
def email_captcha():
    email = request.args.get('email')
    if not email:
        return restful.params_error('请传递邮箱参数！')
    source = list(string.ascii_letters)
    source.extend(map(lambda x: str(x),range(0,10)))
    captcha = "".join(random.sample(source,6))

    #给这个邮箱发送邮件
    message= Message('python论坛验证码',recipients=[email],body='您的邮箱验证码是：%s'% captcha)
    try:
        mail.send(message)
    except :
        return restful.server_error()

    zlcache.set(email,captcha)#邮箱，验证码，存到缓存
    return restful.success()


@cms_bp.route('/email/')
def send_mail():
    message = Message('邮件发送',recipients=['834424581@qq.com'],body='测试')
    mail.send(message)
    return 'success'


cms_bp.route('/posts/')
@login_required
@permission_required(CMSPersmmission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')


cms_bp.route('/comments/')
@login_required
@permission_required(CMSPersmmission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


cms_bp.route('/boards/')
@login_required
@permission_required(CMSPersmmission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')


cms_bp.route('/fusers/')
@login_required
@permission_required(CMSPersmmission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')

cms_bp.route('/cusers/')
@login_required
@permission_required(CMSPersmmission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')

cms_bp.route('/croles/')
@login_required
@permission_required(CMSPersmmission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')


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
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())

cms_bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))
cms_bp.add_url_rule('/resetpwd/',view_func=ResetPwdView.as_view('resetpwd'))
cms_bp.add_url_rule('/resetemail/',view_func=ResetEmailView.as_view('resetemail'))