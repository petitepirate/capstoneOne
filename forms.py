from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length

JOB_TITLES = [("Lead PAM", "Lead PAM"), ("Lead PSO", "Lead PSO"), ("PAM", "PAM Only"), ("PSO", "PSO Only"), ("PSO/PAM", "PSO / PAM Dual Role"), ("Lead PSO/PAM", "Lead PSO & PAM Dual Role")]
LOCATIONS = [("Alaska", "Alaska"), ("Angola", "Angola"),("Antarctica", "Antarctica"),("Arctic Ocean", "Arctic Ocean"),("Argentina", "Argentina"),("Australia / New Zealand", "Australia / New Zealand"),("Black Sea", "Black Sea"),("Brazil", "Brazil"),
("California", "California"),("Canada", "Canada"),("Caribbean", "Caribbean"),("Caspian Sea", "Caspian Sea"),("Chile", "Chile"),("China / Vietnam", "China / Vietnam"),("Columbia", "Columbia"),("Ecuador", "Ecuador"),("Ethiopia", "Ethiopia"),
("Falkland Islands", "Falkland Islands"),("French Guiana", "French Guiana"),("Gabon", "Gabon"),("Ghana", "Ghana"),("Greenland", "Greenland"),("Gulf of Mexico", "Gulf of Mexico"),("Guyana", "Guyana"),("Hawaii", "Hawaii"),("Iceland", "Iceland"),
("India / Sri Lanka", "India / Sri Lanka"),("Indonesia", "Indonesia"),("Madagascar", "Madagascar"),("Malaysia", "Malaysia"),("Mauritania", "Mauritania"),("Mediterranean Sea", "Mediterranean Sea"),("Mexico (Pacific)", "Mexico (Pacific)"),("Mozambique", "Mozambique"),
("Namibia", "Namibia"),("Nigeria", "Nigeria"),("US East Coast (N. Atlantic Ocean)", "US East Coast (N. Atlantic Ocean)"),("North Sea", "North Sea"),("NW Africa / Morocco", "NW Africa / Morocco"),("Persian Gulf", "Persian Gulf"),("Peru", "Peru"),("Philippines", "Philippines"),("Russia", "Russia"),
("Southern China", "Southern China"),("Sierra Leone", "Sierra Leone"),("S. Korea / Japan", "S. Korea / Japan"),("Somalia", "Somalia"),("South Africa", "South Africa"),("Suriname", "Suriname"),("Uruguay", "Uruguay")]
CONT_COMPANIES = [("RPS", "RPS"), ("EPI", "EPI"), ("Atlas", "Atlas"), ("LGL", "LGL"), ("AIS", "AIS"), ("CSA", "CSA"), ("Marine Ventures", "Marine Ventures")]
class NewUserForm(FlaskForm):
    """Form for adding users."""

    user_name = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    # image_url = StringField('(Optional) Image URL')

class LoginForm(FlaskForm):
    """Login form."""

    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

class AddJobForm(FlaskForm):
    """Form for adding Job History"""

    job_title = SelectField(u'Job Title', choices=JOB_TITLES)
    location = SelectField(u'Location', choices=LOCATIONS)
    start_year = IntegerField('Start Year', validators=[DataRequired()])
    day_rate = StringField('Day Rate', validators=[DataRequired()])
    cont_company = SelectField(u"Contracting Company", choices=CONT_COMPANIES)

class EditUserForm(FlaskForm):
    """Edit user form."""
    
    # image_url = StringField('Image URL')
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
