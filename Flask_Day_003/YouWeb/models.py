from YouWeb import db

# Question table class-------------------------------
# column : id, subject, content, created_Date
class Question(db.Model):
    #column name = db.Column(db.type, 제약 조건)
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(),nullable = False)


# Answer table class
# column : id, question_id, question, content, create_date
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete = 'CASCADE'))
    question = db.relationship("Question", backref = db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(),nullable = False)

def get_all_questions():
    return Question.query.order_by(Question.create_date).all()