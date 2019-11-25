from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField, IntegerField
from wtforms import validators


class CreateQueue (FlaskForm):
    date = DateField ("date: ", [
        validators.DataRequired ("Please enter date.")

    ])

    place_name = StringField ("place_name: ", [
        validators.DataRequired ("Please enter place_name.")

    ])

    queue_name = StringField ("queue_name: ", [
        validators.DataRequired ("Please enter queue name.")

    ])
    queue_number = IntegerField ("queue_number: ", [
        validators.DataRequired ("Please enter your queue number.")

    ])
    number_of_people = IntegerField ("number_of_people: ", [
        validators.DataRequired ("Please enter count people.")

    ])
    waiting_time = TimeField ("waititng_time: ", [
        validators.DataRequired ("Please enter waiting_time.")

    ])

    submit = SubmitField ("Save")


class EditQueue (FlaskForm):
    date = DateField ("date: ", [
        validators.DataRequired ("Please enter date.")

    ])

    place_name = StringField ("place_name: ", [
        validators.DataRequired ("Please enter place_name.")

    ])

    queue_name = StringField ("queue_name: ", [
        validators.DataRequired ("Please enter queue name.")

    ])
    queue_number = IntegerField ("queue_number: ", [
        validators.DataRequired ("Please enter your queue number.")

    ])
    number_of_people = IntegerField ("number_of_people: ", [
        validators.DataRequired ("Please enter count people.")

    ])
    waiting_time = TimeField ("waititng_time: ", [
        validators.DataRequired ("Please enter waiting_time.")

    ])

    submit = SubmitField ("Save")
