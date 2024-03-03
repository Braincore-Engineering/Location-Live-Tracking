from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class InsertTrackerForm(FlaskForm):
    name = StringField("Nama", validators=[DataRequired()])
    description = StringField("Deskripsi")
    submit = SubmitField("Submit")
