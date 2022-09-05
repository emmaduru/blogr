from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    body = TextAreaField("Body", validators=[DataRequired()])

class PostCreationForm(PostForm):
    submit = SubmitField("Create Post")

class PostEditForm(PostForm):
    submit = SubmitField("Edit Post")