from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms import validators


class EditCountry (FlaskForm):
    name = StringField("name: ", [
        validators.DataRequired("Please enter name."),
        validators.Length(3,10, "you should input 2<name<10")

    ])

    popultion = StringField("population: ", [
        validators.DataRequired("Please enter your population."),
        validators.NumberRange(min=1000)
    ])

    client_documents = StringField("client_documents: ", [
        validators.DataRequired("Please enter your doc.")

    ])
    goverment = DateField("goverment: ", [
        validators.DataRequired("Please enter goverment.")
    ])
    location = DateField ("location: ", [
        validators.DataRequired ("Please enter location.")
    ])
    submit = SubmitField("Save")


class CreateCountry (FlaskForm):
    name = StringField("name: ", [
        validators.DataRequired("Please enter name.")

    ])

    popultion = StringField("population: ", [
        validators.DataRequired("Please enter your population.")

    ])

    client_documents = StringField("client_documents: ", [
        validators.DataRequired("Please enter your doc.")

    ])
    goverment = DateField("goverment: ", [
        validators.DataRequired("Please enter goverment.")
    ])
    location = DateField ("location: ", [
        validators.DataRequired ("Please enter location.")
    ])
    submit = SubmitField("Save")