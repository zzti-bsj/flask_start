# 1. declare this is a package
# 2. include 工厂函数

import os
from this import d
from flask import Flask

def create_app(test_config=None):
    # create and config the app
    # __name__ 当前模块的名称
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/hello')
    def hello():
        return 'Hello World!'
    
    # 在工厂函数中初始化db
    from . import db
    db.init_app(app)

    return app
