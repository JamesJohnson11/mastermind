from db import db

class PlayerScores(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return '<Player %r>' % self.name