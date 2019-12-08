# -*- encoding: utf-8 -*-
from flask import Flask

app = Flask('blog')


@app.route('/', methods=['GET', ])
def index():
    return 'My flask-blog working!'


application = app.wsgi_app
if __name__ == '__main__':
    app.run()
