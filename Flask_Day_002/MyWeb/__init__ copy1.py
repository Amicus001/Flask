# module
from flask import Flask, render_template, url_for

## Application Factory 기반 Flask Server 구동하기
# Application Factory 기반 함수 정의
def create_app(): # 변경 불가

    #flask server instance
    app = Flask(__name__)

    #blueprint instance: subcategory page route
    #app.register_blueprint()
    @app.route('/')
    def index():
        # return render_template('temp.html')
        return "<h1>It's Time</h1>"

    # data 전송 라우팅 : 변수 < type: 변수명 >
    @app.route('/user/<name>')
    def userinfo(name):
        #return f'<h2>Welcome Back, {name}. </h2>'
        return render_template('temp.html', name=name)
    #test
    with app.test_request_context():
        print(url_for(endpoint='static',filename='css/style_1.css'))
        print(url_for(endpoint='static',filename='image/jellyfish.png')) 

    #Flask Server instance
    return app