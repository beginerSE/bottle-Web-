from bottle import TEMPLATE_PATH, Bottle, debug, redirect, request
from bottle import jinja2_template as template
from bottle import run, static_file


# -------------------------------------------------
# Webサーバ設定
# -------------------------------------------------

app = Bottle()
TEMPLATE_PATH.append(
    "cmd実行してるパスから見た相対パスtemplate")


@app.route('/', method=['GET'])
def index():
    return template('index.html', title='sample_page')


run(app=app)
