from flask import Blueprint,views,render_template

cms_bp = Blueprint('cms',__name__,url_prefix='/cms')


@cms_bp.route('/')
def index():
    return 'cms index'


class LoginView(views.MethodView):
    def get(self):
        return render_template('cms/cms_login.html')

    def post(self):
        pass

cms_bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))