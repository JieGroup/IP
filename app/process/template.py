from __future__ import annotations
from app.error import bad_request

from bson import ObjectId

from app.utils.api import obtain_unique_id

from typing import Any

from app.database.api import (
    search_document,
    create_document,
    update_document
)

from app.utils.api import Time

from app.utils.constant import Constant

from app._typing import Survey_Update_Method


class SurveyTemplate:

    @classmethod
    def if_survey_update_method_valid(
        cls, survey_update_method: str
    ) -> bool:
        
        # TODO: Modify private method later
        return survey_update_method in Survey_Update_Method.__args__

    @classmethod
    def is_number_of_copies_valid(
        cls, number_of_copies: int
    ) -> bool:

        if number_of_copies > Constant.MAX_NUMBER_OF_COPIES:
            return False
        return True

    @classmethod
    def if_survey_topics_valid(
        cls, 
        survey_update_method: Survey_Update_Method,
        time_period: int,
        number_of_copies: int,
        survey_topics: dict[dict[str, Any]]
    ) -> None:

        error_message = {}

        # Check if survey_update_method is in defined category
        if not cls.if_survey_update_method_valid(
            survey_update_method=survey_update_method
        ):
            error_message['survey_update_method'] = 'Please provide a valid survey topics update method'

        # Check if the time_period is within 2 months
        if not Time.is_time_period_valid(time_period):
            error_message['time_period'] = 'Please provide a time period between 1 and 60 days'

        # Check if the number of copies is within maximum number
        # of copies
        if not cls.is_number_of_copies_valid(number_of_copies):
            error_message['number_of_copies'] = 'Please provide a number of copies between 1 and 500'
            
        # TODO: Check Survey_topics. Not urgent
        return error_message

    @classmethod
    def create_survey_template(
        cls, 
        survey_update_method: Survey_Update_Method,
        time_period: int,
        number_of_copies: int,
        survey_topics: dict[dict[str, Any]]
    ) -> None:

       
        '''
            Check new survey template information and store
            the survey template information in db.
        '''
        
        # Check the survey topics uploaded by user
        validation_res = cls.if_survey_topics_valid(
            survey_update_method=survey_update_method,
            time_period=time_period,
            number_of_copies=number_of_copies,
            survey_topics=survey_topics
        )
        # If validation_res != {}, it means we have error message.
        # We need to return error message
        if validation_res:
            return bad_request(validation_res)

        # Store the new template
        newObjectId = ObjectId()
        survey_template_id=str(newObjectId)
        expiration_time = Time.get_expiration_time(time_period)
        create_document(
            database_type='survey_template',
            survey_template_id=survey_template_id,
            survey_update_method=survey_update_method,
            expiration_time=expiration_time,
            number_of_copies=number_of_copies,
            survey_topics=survey_topics
        )

        return survey_template_id
    

    # @classmethod
    # def update_survey_template(
    #     cls, 
    #     survey_template_id: str,
    #     root_key: str
    # ) -> None:

    #     # check if root_key is matched
    #     document = search_document(
    #         database_type='survey_template',
    #         survey_template_id=survey_template_id,
    #         root_key=root_key
    #     )

    #     if document == None:
    #         return False

    #     # count current time of template
    #     current_times_of_template = document['current_times_of_template'] + 1

    #     return update_document(
    #         database_type='survey_template',
    #         survey_template_id=survey_template_id,
    #         current_times_of_template=current_times_of_template
    #     )

    

# from flask_wtf import FlaskForm
# from wtforms import (
#     StringField, SubmitField, RadioField, SelectField,
#     SelectMultipleField, TextAreaField)
# # from wtforms.fields.html5 import EmailField, IntegerField
# from wtforms.fields import EmailField, IntegerField
# # from wtforms.widgets import html5 as h5widgets
# from wtforms.widgets import CheckboxInput, ListWidget
# from wtforms.validators import ValidationError, DataRequired, Length, Optional, InputRequired, NumberRange
# from app.utils import *


# class FrontForm(FlaskForm):
    
#     # name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])

#     # email = EmailField('Email', validators=[DataRequired(), Length(min=2, max=20)])

#     # value = RadioField(sentence, choices=choices, validators=[DataRequired()])
#     submit = SubmitField('Start')


# # currently support dynamical number of questions on a form
# def DynammicForm(questions: dict):
#     '''
#         generate a from for dynamic survey questions
#         the html can only show static form, so we use a way to wrap
#         see the solution from 
#         https://stackoverflow.com/questions/51599936/how-do-i-bind-an-flask-wtform-unboundfield

#     '''

#     class Form(FlaskForm):

#         # name = StringField('Name', validators=[DataRequired(), Length(max=100)])
#         # 'next' is shown in the button
#         submit = SubmitField('Next')

#     # dynamic question
#     for topic, (param, sentence, choices) in questions.items():
        
#         if topic != 'MTurk':
#             value = RadioField(sentence, choices=choices, validators=[DataRequired()])

#         else: 
#             value = StringField(sentence, validators=[InputRequired()])

#         setattr(Form, topic, value)

#     return Form()


# def StaticForm(questions: dict):
#     '''
#         generate a from for static survey questions
#     '''

#     class Form(FlaskForm):

#         submit = SubmitField('Next')

#     # dynamic question
#     for topic, (param, sentence, choices) in questions.items():
        
#         if param == 'RadioField':

#             # choices: list of tuples
#             value = RadioField(sentence, choices=choices, validators=[DataRequired()])

#         elif param == 'SelectField':

#             # choices: list of tuples
#             value = SelectField(sentence, choices=choices, validators=[DataRequired()])

#         elif param == 'IntegerField':

#             # choices: list of lower and upper limits
#             if topic != 'spouse_age':
#                 value = IntegerField(sentence, validators=[InputRequired()])
#             else:
#                 value = IntegerField(sentence, validators=[Optional()])
#                  # widget=h5widgets.NumberInput(min=choices[0], max=choices[1]))
#             # NOTE: the above min-max constraint was commented not because of tech reason
#             # because the range may offend the respondents, while we need a reasonable range for interval data

#         elif param == 'StringField':
            
#             value = StringField(sentence, validators=[InputRequired()])

#         else:
#             debug('wrong param for StaticForm!')

#         setattr(Form, topic, value)

#     return Form()
