from flask import Flask
from apps.cms import cms_bp
from apps.common import common_bp
from apps.front import front_bp
import config

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(cms_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)

if __name__ == '__main__':
    app.run()
