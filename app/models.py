from app import db
from flask_login import UserMixin

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,title,content,user_id):
        self.title = title
        self.content = content
        self.user_id = user_id
    
    @property
    def serialize(self):
        return {
           'title':self.title,
           'content':self.content,
           'text_id':int(self.id),
        }

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    texts = db.relationship('Text',backref='user',lazy=True)

    def __init__(self,username, password):
        self.username = username
        self.password = password