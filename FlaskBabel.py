from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config["BABEL_DEFAULT_LOCALE"] = "zh_CN"
babel = Babel(app)

LANGUAGES = {
    'en': 'English',
    "zh": "zh_CN"
}




@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())


@app.route('/')
def hello_world():
    day = _("Saturday")
    return render_template("index.html", day=day)


if __name__ == '__main__':
    app.debug = True
    app.run()
