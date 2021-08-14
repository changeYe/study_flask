from flask import Flask


# 文件夹中有__init__文件，就会把当前文件夹做为包导入

# 注册蓝图
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)


# 创建app,同时要调用注册蓝图的方法
def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app
