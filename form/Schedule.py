from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField
from wtforms import validators


class CreateSchedule (FlaskForm):
    time_in_queue = TimeField ("time: ", [
        validators.DataRequired ("Please enter your time.")

    ])

    date = DateField ("date: ", [
        validators.DataRequired ("Please enter date.")

    ])
    push_notification = StringField ("not: ", [
        validators.DataRequired ("Please enter your not.")
    ])

    submit = SubmitField ("Save")



class EditSchedule (FlaskForm):
    time_in_queue = TimeField ("time: ", [
        validators.DataRequired ("Please enter your time.")

    ])

    date = DateField ("date: ", [
        validators.DataRequired ("Please enter date.")

    ])
    push_notification = StringField ("not: ", [
        validators.DataRequired ("Please enter your not.")
    ])

    submit = SubmitField ("Save")
