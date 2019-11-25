from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators


class CreatePlace (FlaskForm):
    place_name = StringField ("place_name: ", [
        validators.DataRequired ("Please enter place name.")

    ])

    place_site = StringField ("place_site: ", [
        validators.DataRequired ("Please enter site.")

    ])

    type_of_service = StringField ("type_of_service: ", [
        validators.DataRequired ("Please enter your service.")

    ])

    submit = SubmitField ("Save")


class EditPlace (FlaskForm):
    place_name = StringField ("place_name: ", [
        validators.DataRequired ("Please enter place name.")

    ])

    place_site = StringField ("place_site: ", [
        validators.DataRequired ("Please enter site.")

    ])

    type_of_service = StringField ("type_of_service: ", [
        validators.DataRequired ("Please enter your service.")

    ])

    submit = SubmitField ("Save")
