
from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__,
            static_url_path='/python',  # 访问静态资源的url前缀，默认是static
            static_folder='static',  # 静态文件目录，默认是static
            template_folder='templates',  # 模板文件目录，默认是templates
            )


# 1.自定义转换器
class RegexConverter(BaseConverter):
    """description"""
    def __init__(self, url_map, regex):
        """docstring for __init__"""
        # 调用父类方法初始化方法
        super().__init__(url_map)
        # 将正则表达式保存到对象的属性中，flask会去使用这个属性进行正则匹配
        self.regex = regex

    def to_python(self, value):
        # value是在正则表达式匹配时提取的参数
        return value

    def to_url(self, value):
        """使用url_for的时候被调用"""
        return value


# 2.将转换器绑定到flask应用中
app.url_map.converters['re'] = RegexConverter

# 3.localhost:5000/17123456789
@app.route("/send/<re(r'1[34578]\d{9}'):phone>")
def send(phone):
    """docstring for send"""
    return "手机号码：{0}".format(phone)


@ app.route("/index")
def indexT():
    # 使用自定义转换器
    url = url_for("send", phone="17812345678")
    # localhost:5000/send
    return redirect(url)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(app.url_map)
    return "hello"


@app.route('/greet/', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello，%s!<h1>' % name


@app.route('/hello', methods=['POST'])
def hello1():
    return "hello 1"


@app.route('/hello', methods=['GET'])
def hello2():
    return "hello 2"

# @app.cli.command()
#  def hello():
#   click.echo('Hello!')
