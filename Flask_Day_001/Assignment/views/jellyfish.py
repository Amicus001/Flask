from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/main/') # 주소창에 '/main/' 필수

@bp.route('/jellyfish')
def jellyfish():
    return 'this is jellyfish 🪼'

@bp.route('/lion_mane_jellyfish')
def lion_mane_jellyfish():
    return 'this is lion mane jellyfish'
