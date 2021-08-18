from flask import jsonify, request

from app.libs.Helper import is_keyword
from app.spider.YuShu_Book import Yushu_Book
from app.forms.param_valid import SearchForm
from app.web.my_blueprint import web


# 获取get请求的参数： 通过request.args 获取
@web.route("/hello")
def hello():
    # p = request.args['p']
    # page = request.args['page']
    # print('这是请求参数 %s 页码 %s' %(p, page))
    dicta = request.args.to_dict()
    form = SearchForm(request.args)
    p = form.p.data.strip()
    page = form.page.data
    print('这是请求参数 %s 页码 %s' % (p, page))
    if form.validate():
        print('验证成功')
        return 'hello world'
    else:
        return jsonify(form.errors)


@web.route("/book/search/<p>/<page>")
def search(p, page):
    # 判断p参数的类型：是数字还是字符串
    is_keyword_flag = is_keyword(p)
    if is_keyword_flag == 'isbn':
        result = Yushu_Book.search_isbn(p)
    else:
        result = Yushu_Book.search_keyword(p)
    return jsonify(result)
