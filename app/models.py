from app import db
import datetime

class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True) # Amazon mturk ID
    qa = db.relationship('QandA', backref='voter', lazy='dynamic')

    def __repr__(self):
        return f'<Voter {self.name}>'


class QandA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.DateTime, default=datetime.datetime.now)
    endtime = db.Column(db.DateTime, default=datetime.datetime.now)
    way = db.Column(db.String(20))  # currently support 'dynamic' or 'static'
    topic = db.Column(db.String(20))
    param = db.Column(db.Integer)
    answer = db.Column(db.String(20))
    rounds = db.Column(db.Integer) # how many times the pair of question and voter
    digits = db.Column(db.String(20)) # token to the survey
    # the following will be filled during the post-processing of what Qin receives from mturk
    surveyround = db.Column(db.Integer) # the round (1-5) that the question-answer belongs to
    voter_id = db.Column(db.Integer, db.ForeignKey('voter.id'))
    mturkID = db.Column(db.String(50), index=True) # mturkID, real Id of voter

    def __repr__(self):
        return f'<Topic: {self.topic}, Param: {self.param}, Answer: {self.answer}, \
        rounds: {self.rounds}, surveyround: {self.surveyround}, voter_id: {self.voter_id}>'
