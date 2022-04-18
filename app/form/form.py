from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField, RadioField, SelectField,
    SelectMultipleField, TextAreaField)
# from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.fields import EmailField, IntegerField
# from wtforms.widgets import html5 as h5widgets
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms.validators import ValidationError, DataRequired, Length, Optional, InputRequired, NumberRange
from app.utils import *


class FrontForm(FlaskForm):
    
    # name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])

    # email = EmailField('Email', validators=[DataRequired(), Length(min=2, max=20)])

    # value = RadioField(sentence, choices=choices, validators=[DataRequired()])
    submit = SubmitField('Start')


# currently support dynamical number of questions on a form
def DynammicForm(questions: dict):
    '''
        generate a from for dynamic survey questions
        the html can only show static form, so we use a way to wrap
        see the solution from 
        https://stackoverflow.com/questions/51599936/how-do-i-bind-an-flask-wtform-unboundfield

    '''

    class Form(FlaskForm):

        # name = StringField('Name', validators=[DataRequired(), Length(max=100)])
        # 'next' is shown in the button
        submit = SubmitField('Next')

    # dynamic question
    for topic, (param, sentence, choices) in questions.items():
        
        if topic != 'MTurk':
            value = RadioField(sentence, choices=choices, validators=[DataRequired()])

        else: 
            value = StringField(sentence, validators=[InputRequired()])

        setattr(Form, topic, value)

    return Form()


def StaticForm(questions: dict):
    '''
        generate a from for static survey questions
    '''

    class Form(FlaskForm):

        submit = SubmitField('Next')

    # dynamic question
    for topic, (param, sentence, choices) in questions.items():
        
        if param == 'RadioField':

            # choices: list of tuples
            value = RadioField(sentence, choices=choices, validators=[DataRequired()])

        elif param == 'SelectField':

            # choices: list of tuples
            value = SelectField(sentence, choices=choices, validators=[DataRequired()])

        elif param == 'IntegerField':

            # choices: list of lower and upper limits
            if topic != 'spouse_age':
                value = IntegerField(sentence, validators=[InputRequired()])
            else:
                value = IntegerField(sentence, validators=[Optional()])
                 # widget=h5widgets.NumberInput(min=choices[0], max=choices[1]))
            # NOTE: the above min-max constraint was commented not because of tech reason
            # because the range may offend the respondents, while we need a reasonable range for interval data

        elif param == 'StringField':
            
            value = StringField(sentence, validators=[InputRequired()])

        else:
            debug('wrong param for StaticForm!')

        setattr(Form, topic, value)

    return Form()
