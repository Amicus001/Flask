### ==> 기능 : main 범주의 url 라우팅
## --> url: /main, /main/info, /main/about, etc.

from flask import Blueprint
bp = Blueprint('main', __name__, url_prefix='/main/')

@bp.route('about')
def about(about):
    return 'THIS IS A MAIN_ABOUT PAGE'
