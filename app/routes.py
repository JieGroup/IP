from flask import render_template, flash, redirect, url_for, request, session, make_response
from app import app, db
from app.models import Voter, QandA
from app.form import FrontForm, DynammicForm, StaticForm
import numpy as np
import sys
from datetime import datetime, timezone
from app.constant import *
from wtforms import RadioField
from wtforms.validators import InputRequired
from random import Random
from sqlalchemy import desc
import string
import random


# define fixed TYPE of entry to either random, dynamic, or static survey
RAN = '1mACBzA4ktv9fEEPfcXh8RB6' # http://0.0.0.0:8000/1mACBzA4ktv9fEEPfcXh8RB6
DYN = 'ZrovHUMI0wZE8DdPNI6WElY3' # http://0.0.0.0:8000/ZrovHUMI0wZE8DdPNI6WElY3
STA = 'ypnWYpfb5dLEQ6xWfiALTVqH' # http://0.0.0.0:8000/ypnWYpfb5dLEQ6xWfiALTVqH

# to publish: 
# http://3.141.9.233:8000/1mACBzA4ktv9fEEPfcXh8RB6 
# http://3.141.9.233:8000/ZrovHUMI0wZE8DdPNI6WElY3
# http://3.141.9.233:8000/ypnWYpfb5dLEQ6xWfiALTVqH

# SIMPLE_CHARS = string.ascii_letters + string.digits
SIMPLE_CHARS = string.digits
def get_random_digits(length=8):
    return ''.join(random.choice(SIMPLE_CHARS) for i in range(length))


# front page that introduces the survey and record user info
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/front', methods=['GET', 'POST'])
@app.route('/<string:typ>', methods=['GET', 'POST'])
def front(typ):

    # clean upon entry
    if '_flashes' in session:
            session.pop('_flashes', None)

    form = FrontForm()

    # make sure the voter submits only one time
    if 'submitted' in session:
        pass
        # flash(f"The survey of the link has been completed. Thank you!")
        # return render_template('front2.html', form=form)

    # equiv to check if request.method == 'POST' and if valid_login(request.form)
    if form.validate_on_submit():

        # initialize session once the voter submits basic info and starts survey
        session['start_time'] = datetime.now(timezone.utc)
        session['progress_bar'] = 0
        session['digits'] = get_random_digits()
        session['entered_MTurk'] = False
        
        # generate a randseed specific for this voter
        randseed = int(session['digits']) * MAXREP

        # settle the type of the survey
        if typ == RAN:
            # randomly determine which survey way to use
            myRandom = Random(randseed)
            session['survey_way'] = myRandom.sample(SURVEY_WAY, 1)[0]

        elif typ == DYN:
            session['survey_way'] = 'dynamic'

        elif typ == STA:
            session['survey_way'] = 'static'

        else:
            debug('not the right type!')

        return redirect(url_for('question', randseed=randseed))

    return render_template('front2.html', form=form)


# end page that thanks the survey
@app.route('/end', methods=['GET'])
def end():

    # create a session key-value that has 30min default expiration
    # to ensure the user does not submit immediately again
    session['submitted'] = True

    # create a cookie that lasts 12 hours, to ensure the voter cannot log in after restart browser
    # currently failed to work after restarting browser
    # resp = make_response(render_template('end.html'))
    # resp.set_cookie("voter-submitted", '1', 60*60*12)
    # return resp

    return render_template('end.html', digits=session['digits'])


# question page that asks a dynamically generated list of question
# conditional on the previous answers (by default stored in request)
# previously we used voter_id to query how many rounds the voter has answered a question, now we can use the
# digits (also unique) to identify the round
@app.route('/q/<string:randseed>', methods=['GET', 'POST'])
def question(randseed):

    # debug(f'{voter_id}, {randseed}, {tok}', 'enter question')
    # debug(db.session.query(QandA).order_by(QandA.endtime).first(), 'current db->QandA')

    # fetch the set of feasible questions
    if session['survey_way'] == 'dynamic':
        questions = gen_dynamic_questions(randseed)
        form = DynammicForm(questions)

    elif session['survey_way'] == 'static':
        questions = gen_static_questions(randseed)
        form = StaticForm(questions)

    else:
        debug('Wrong survey_way!')

    # debug(questions.keys(), 'topics')

    if not questions:

        flash(f"Thanks, you have completed the survey!")

        return redirect(url_for('end'))

    # equiv to check if request.method == 'POST' and if valid_login(request.form)
    if form.validate_on_submit():

        for topic, (param, sentence, choices) in questions.items():

            answer = str(form.data[topic]) # we required str field in the database
            # rounds = db.session.query(QandA).filter_by(voter_id=voter_id, topic=topic).count()
            rounds = db.session.query(QandA).filter_by(digits=session['digits'], topic=topic).count()

            if topic == 'MTurk':
                session['entered_MTurk'] = True # one time lock

            # debug(topic, 'topic')

            # add time stamp
            qa = QandA(
                starttime=session['start_time'],
                endtime=datetime.now(timezone.utc),
                way=session['survey_way'],
                topic=topic,
                param=param,
                answer=answer,
                rounds=rounds+1,
                digits=session['digits']
                )

            db.session.add(qa)
            db.session.commit()

        flash(f"Thanks, you have completed {session['progress_bar']}% of the survey!")

        # note that the randseed became string type because of @app.route coercion
        return redirect(url_for('question', randseed=int(randseed)+1))

    # else:
    #     print('Jie debug logic', file=sys.stdout)

    return render_template('question.html', form=form)
