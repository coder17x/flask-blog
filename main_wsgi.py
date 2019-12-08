# -*- encoding: utf-8 -*-
import os
import sys

from flask import Flask, render_template

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_PATH)

app = Flask('blog', static_folder="../static")

# DEBUG
app.debug = True
app.config.EXPLAIN_TEMPLATE_LOADING = True
# END DEBUG


@app.route('/', methods=['GET', ])
def index():
    return render_template("index.html.j2", title="Blog site")


application = app.wsgi_app
if __name__ == '__main__':
    app.run()
