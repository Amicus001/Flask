## -----------------------------------------------------------------
# 데이터 저장 및 출력 관련  웹 페이지 라우팅 처리 블루프린트
# URL: /input *prefix
#      /input/save
#      /input/delete
#      /input/update
## -----------------------------------------------------------------

from flask import Blueprint, render_template, request

#bp instance
databp = Blueprint(name='DATA', 
                   import_name= __name__,
                   static_folder='templates', 
                   url_prefix='/input')


#routing functions

@databp.route('/') # http://127.0.0.1:5000/input/
def input_data():
    return render_template('input_data.html', 
                           action='/input/save_post',
                           method = 'POST')


#data save by get method
#save in user request object
#@databp.route('/save_get') 


# save / post 방식 합쳐서 하나의 함수로 만들기. 
@databp.route('/save', methods = ['POST','GET'])
def save():
    method = request.method
    if method == ['POST']:
        
        header= request.headers
        method = request.method
        args = request.args.to_dict()
        v = request.form['value']
        m = request.form['message']
        return f"✨✨SAVE POST DATA✨✨<br>method:{method}<br>headers:{header}<br>args:{args}<br>values:{v}<br>message:{m}<br>"
    if method == ['GET']:
        req_dict = request.args.to_dict()
    # v = req_dict.get('value')
    # msg = req_dict.get('message')
    #return f"✨✨SAVE GET DATA✨✨"
        return render_template('save_data.html',**req_dict)#value = v,message = msg, )#**req_dict)



# http://127.0.0.1
def save_get_data():
    #요청 데이터 추출하기
    req_dict = request.args.to_dict()
    # v = req_dict.get('value')
    # msg = req_dict.get('message')
    #return f"✨✨SAVE GET DATA✨✨"
    return render_template('save_data.html',**req_dict)#value = v,message = msg, )#**req_dict)



# data save by post method
@databp.route(rule = '/save_post', methods = ['POST']) # http://127.0.0.1
def save_post_data():
    header= request.headers
    method = request.method
    args = request.args.to_dict()
    v = request.form['value']
    m = request.form['message']
    return f"✨✨SAVE POST DATA✨✨<br>method:{method}<br>headers:{header}<br>args:{args}<br>values:{v}<br>message:{m}<br>"
   
   
  # return render_template('save_data.html', )