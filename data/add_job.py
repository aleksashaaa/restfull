from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('title', validators=[DataRequired()])
    team_leader = IntegerField('team leader id', validators=[DataRequired()])
    work_size = StringField('work size', validators=[DataRequired()])
    collaborators = StringField('collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')

    submit = SubmitField('Submit')