
from bottle import TEMPLATE_PATH, Bottle, debug, redirect, request
from bottle import jinja2_template as template
from bottle import run, static_file


# -------------------------------------------------
# Webサーバ設定
# -------------------------------------------------

app = Bottle()
debug(debug_mode)
TEMPLATE_PATH.append("/template")


@app.route('/index', method=['GET'])
def index():
    return template('index.html)
                    
                    

run(app=app, server='paste', host=host, port=port)
