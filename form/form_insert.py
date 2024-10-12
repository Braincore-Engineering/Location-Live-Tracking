from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class InsertTrackerForm(FlaskForm):
    name = StringField("Nama", validators=[DataRequired()])
    description = StringField("Deskripsi", validators=[DataRequired()])
    asset_img_url = StringField("Foto Aset", validators=[DataRequired()])
    tracker_img_url = StringField("Foto Tracker", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])
