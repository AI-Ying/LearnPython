from flask import Flask, request, jsonify, session,\
                  make_response, url_for, redirect, abort, Response, \
                  session
# from flask_script import Manager
import json, os

app = Flask(__name__)

# manager = Manager(app)

# 127.0.0.1:5000?city=Beijing&country=china&city=nanchang  ？后面的是查询字符串
# POST和GET一样也可以使用查询字符串
@app.route('/', methods=['GET', 'POST'])
def index():

    # request中包含了前端发送过来的所有请求数据
    # form 和 data用来提取请求体数据
    # request.form可以直接提取请求体的表单数据，是字典类对象
    # 通过get方法只能拿到同名参数的第一个，可以通过getlist方法获取同名参数列表
    name = request.form.get("name")
    age = request.form.get("age")
    name = request.form.get("name")
    name_list = request.form.getlist("name")

    # args 是用来提取url中的参数（查询字符串）
    city = request.args.get("city")
    country = request.args.get("country")
    city = request.args.get("city")
    city_list = request.args.getlist("city")

    # 如果请求的数据不是表单格式（如json格式），可以通过request.data获取
    print("request.data:{0}".format(request.data))

    # if request.methods == 'GET':
    #     pass
    # elif request.methods == 'POST':
    #     pass

    return '<h1>Hello {0}, age = {1}, city={2}, country={3}, form_list={4}, city_list={5}</h1>'\
        .format(name, age, city, country, name_list, city_list)


@app.route('/upload', methods=['POST'])
def upload():
    f_obj = request.files.get("pic")
    if f_obj is None:
        return "未上传文件"

    # 方法一：
    # 1.创建一个文件
    # f = open('./demos/http/demo.png', 'wb')
    # 2.向文件写入内容
    # data = f_obj.read()
    # f.write(data)
    # 3.关闭文件
    # f.close()

    # 方法二：open会自动关闭打开的文件
    # with open('./demos/http/demo.png', 'wb') as f:
    #     f.write(f_obj.read())

    # 方法三：flask 自带函数
    f_obj.save('./demos/http/demo.png')
    return "上传成功"


@app.route('/res')
def res():
    # 1. 使用元组，返回自定义信息
    #        响应体，状态码，响应头
    # return "index", 666, [("name", "ai"), ("city", "Beijing")]
    # return "index", 666, {"name": "ai", "city": "Beijing"}
    # return "index", "666 statuscode description",

    # 2. 使用make_response 来构造响应信息
    resp = make_response("index page")
    resp.status = "999 status description"
    resp.headers['city'] = 'Beijing'
    return resp


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))


@app.route('/set/<name>')
def set(name):
    response = make_response(redirect(url_for('hello', name=name)))
    response.set_cookie('name', name)
    return response


@app.route('/json')
def json_res():
    data = {
        "city": "Beijing",
        "country": "china"
    }

    # # 1.使用内置函数
    # json.dumps(dic) 将python中的字典转换成字符串
    # json.loads(str) 将字符串转换成python中的字典
    # json_str = json.dumps(data)
    # # 如果不设置content-type的话， 返回的类型仍是application/text
    # return json_str
    # return json_str, 500, {"Content-Type": "application/json"}

    # flask内置函数,导入jsonify,帮助转为python数据，并设置响应头Content-Type 为
    # appliction/json
    return jsonify(data)
    # return jsonify(name='Grey Li', gender='male'), 500


@app.route('/set_cookie')
def set_cookie():
    """docstring for set_cookie"""
    # 设置cookie，默认是临时cookie，浏览器关闭就失效
    res = make_response('success')
    res.set_cookie('name1', 'ai')
    res.set_cookie('name2', 'ying')
    # 设置有效期，单位秒
    res.set_cookie('name3', 'tom', max_age=3600)

    # 通过header来设置cookie
    res.headers['Set-Cookie'] = "name4=join; Expires=Thu," \
        + "28-Feb-2019 08:30:14 GMT; Max-Age=3600; Path=/"

    return res


@app.route('/get_cookie')
def get_cookie():
    # 获取cookie
    cookie = request.cookies.get('name3')
    return cookie


@app.route('/delete_cookie')
def delete_cookie():
    res = make_response('delete_cookie')
    res.delete_cookie('name3')
    return res


@app.route('/note')
def foo():
    response = make_response('Hello')
    response.mimetype = 'text/plain'
    return response


@app.route('/secret')
def secret():
    """docstring for secret"""
    # 从.env文件中获取SECRET_KEY, 如果SECRET_KEY为空，那么使用默认的第二个参数作为SECRET_KEY
    app.secret_key = os.getenv('SECRET_KEY', 'ksjdaksdfjak8934523kjfka')
    return app.secret_key


@app.route('/set_session')
def set_session():
    # flask的session使用需要使用SECERT_KEY
    app.secret_key = os.getenv('SECRET_KEY', 'ksjdaksdfjak8934523kjfka')
    # flask 默认把session保存在cookie中
    print(app.secret_key)
    session['name'] = 'ai'
    return 'login sucess'


@app.route('/hello')
@app.route('/hello/<name>')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name')
    return '<h1>Hello {0}</h1>'.format(name)


@app.route('/goback/<int:year>')
def goback(year):
    return '<p> Welcome to %d.' % (2019-year)


@app.route('/bar')
def bar():
    return '<h1> Foo Page</h1><a href="{}">Do something and redirect</a>'\
        .format(url_for('hello', next=request.full_path))


@app.route('/hook')
def hook():
    """docstring for hook"""
    # 1/0
    print('hook test')
    return 'hook test'


@app.before_first_request
def hand_before_first_request():
    # 第一次请求处理前被执行
    print("hand_before_first_request():第一次请求处理前被执行")


@app.before_request
def hand_before_request():
    # 每次请求处理前被执行
    print("hand_before_request():每次请求处理前被执行")


# @app.after_this_request
# def hand_after_this_request(res):
#     # 某个视图函数请求处理后被执行, 必须带有响应对象参数
#     print("hand_after_this_request(res):某个视图函数请求处理后被执行")
#     return res


@app.after_request
def hand_after_request(res):
    # 每次请求视图函数处理后执行，前提是视图函数没有异常
    print("hand_after_request(res):每次请求视图函数处理后执行，前提是视图函数没有异常")
    return res


@app.teardown_request
def hand_teardown_request(res):
    # 每次请求视图函数处理后执行，无论视图函数是否有异常, 前提必须实在生产模式，即Debug=False
    print("hand_teardown_request(res):# 每次请求视图函数处理后执行，无论视图函数是否有异常")
    return res


@app.route('/abort')
def abort_error():
    name = request.form.get('name')
    age = request.form.get('age')
    if name == 'ai' and age == 18:
        return "name={0}, age={1}".format(name, age)
    else:
        # 1.返回状态码(常用)
        abort(404)
        # 2.返回响应体信息
        # res = response("failed")
        #  abort(res)


# 自定义错误方法
@app.errorhandler(404)
def error(err):
    return "自定义错误方法{0}".format(err)
