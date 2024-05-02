from flask import Blueprint, render_template

bp = Blueprint(name='main',
               import_name= __name__,
               template_folder= 'templates',
               url_prefix='/')

#routing function
@bp.route('/admin/question/submitted')
def index():
    # Question table 읽어서 출력하기
    from YouWeb.models import Question
    question_list = Question.query.order_by(Question.create_date.desc())
    
    return render_template('question_list.html', question_list = question_list)


@bp.route('/admin/question')
def question():
    return render_template('insert.html')

# @bp.route('/admin/question/submitted')
# def submitted():
#     from YouWeb.templates import submitted
#     question_list = 
#     return render_template('submitted.html')