# from flask import Flask
from app import create_app
# app = Flask(__name__)

# 添加url地址
# app.add_url_rule("/hello",view_func=hello)

# 这里通过app手动加载配置文件，参数是模版路径,通过app.config['DEBUG']调用，config是dict子类
# app.config.from_object('config')
#
# print(str(id(app)) + " 这是创建中")
# 导入book文件
# from app.web import book


app = create_app()

# 添加这个判断的原因是导入这个文件不会执行app.run方法
# 只有通过python启动这个文件时，才会执行app.run,python一般通过nginx+uwsgi 启动python程序，
# 所以不会执行app.run方法
if __name__ == '__main__':
    print(str(id(app))+" 这是main中")
    app.run(host='0.0.0.0', debug=app.config['DEBUG'],port=8090)