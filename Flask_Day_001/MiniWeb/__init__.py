# module
from flask import Flask, render_template, Blueprint


### application factory functions
def create_app():
    myapp = Flask(__name__)

    #bp 등록
    from.views import main_views
    myapp.register_blueprint(main_views.bp)


    return myapp
##
# 전역 변수
# myapp = Flask(import_name=__name__) #flask instance

# # 사용자 요청 url 처리 기능: 라우팅Routing
# # 형식 : @Flask_instance_name.route(urlstring)
# @myapp.route('/') # web server first page: https://127.0.0.1:5000/


# def index_page(): #화면에 출력할 애
#     #return "<h3><font color='blueviolet'>MyWeb IndexPage</font></h3>"
#     return render_template('temp.html') # 미리 만들어둔 temp.html 파일을 템플릿으로 사용한다



# # 사용자마다 다른 페이지 반환
# ## 사용자 페이지 = https://127.0.0.1:5000/<username>
# @myapp.route(rule='/<name>')# </어쩌고> : 변수이름. 홑화살괄호가 없으면 그냥 스트링으로 들어간다. 
# def username(name):
#     return f"username : {name}"

# # 숫자를 받는 페이지 반환
# @myapp.route(rule='/<int:number>')
# def number(number):
#     return f'selected number : {number}'    

# # 라우팅
# @myapp.route('/userinfo')
# def usrelogin():
#     return myapp.redirect('/')


# #running control
# if __name__ == '__main__':
#     # run Flask web server
  
#     myapp.run(debug=True) #run the web server
