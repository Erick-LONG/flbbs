from flask import (
    Blueprint,
    views,
    render_template,

)

front_bp = Blueprint('front',__name__)

@front_bp.route('/')
def index():
    return 'front index'


class SignupView(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')


front_bp.add_url_rule('/signup/',view_func=SignupView.as_view('signup'))