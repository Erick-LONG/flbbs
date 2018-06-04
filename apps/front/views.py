from flask import (
    Blueprint,
    views,
    render_template,
    make_response
)

from utils.captcha import Captcha
from io import BytesIO

front_bp = Blueprint('front',__name__)


@front_bp.route('/')
def index():
    return 'front index'


@front_bp.route('/captcha/')
def graph_captcha():
    #获取验证码
    text,image = Captcha.gene_graph_captcha()
    #BytesIO,字节流
    out = BytesIO()
    image.save(out,'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


class SignupView(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')


front_bp.add_url_rule('/signup/',view_func=SignupView.as_view('signup'))