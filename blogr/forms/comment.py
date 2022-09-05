from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CommentCreationForm(FlaskForm):
    body = TextAreaField(validators=[DataRequired()])
    submit = SubmitField("Add Comment")