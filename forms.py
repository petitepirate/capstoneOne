# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, TextAreaField
# from wtforms.validators import DataRequired, Email, Length

# class NewUserForm(FlaskForm):
#     """Form for adding users."""

#     user_name = StringField('Username', validators=[DataRequired()])
#     first_name = StringField('First Name', validators=[DataRequired()])
#     last_name = StringField('Last Name', validators=[DataRequired()])
#     email = StringField('E-mail', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[Length(min=6)])
#     image_url = StringField('(Optional) Image URL')

# class LoginForm(FlaskForm):
#     """Login form."""

#     user_name = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[Length(min=6)])
