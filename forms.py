from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

class AddressForm(Form):
  address = StringField('Address', validators=[DataRequired("Please enter an address.")])
  submit = SubmitField("Search")

class ActivityForm(Form):
  name = StringField('Name', validators=[DataRequired("Please enter the name of the activity.")])
  address = StringField('Address', validators=[DataRequired("Please enter the address.")])
  description = StringField('Description', validators=[DataRequired("Please enter a description of the activity.")])
  age = StringField('Age', validators=[DataRequired("Please enter the age range (Toddler, Young Children, Teens, Adults)")])
  fee = StringField('Fee', validators=[DataRequired("Please enter 'free' or 'fee'.")])
  submit = SubmitField('Submit')

class ActivityForm2(Form):
  name = StringField('Name', validators=[DataRequired("Please enter the name of the activity.")])
  address = StringField('Address', validators=[DataRequired("Please enter the address.")])
  description = StringField('Description', validators=[DataRequired("Please enter a description of the activity.")])
  age1 = BooleanField('Young Children')
  age2 = BooleanField('Children')
  age3 = BooleanField('Teens')
  age4 = BooleanField('Adults')
  age5 = BooleanField('All Ages')
  price1 = BooleanField('Free')
  price2 = BooleanField('Fee')
  cat1 = BooleanField('Active camps')
  cat2 = BooleanField('Active Games: Equipment Needed')
  cat3 = BooleanField('Active Games: No Equipment Needed')
  cat4 = BooleanField('Aquatics')
  cat5 = BooleanField('Ball Sports')
  cat6 = BooleanField('Dance')
  cat7 = BooleanField('Fitness')
  cat8 = BooleanField('Gymnastics/Tumbling')
  cat9 = BooleanField('Martial Arts')
  cat10 = BooleanField('Mind body')
  cat11 = BooleanField('Playgrounds')
  cat12 = BooleanField('Recreation Spaces')
  cat13 = BooleanField('Trails/Paths')
  website = StringField('Website', validators=[DataRequired("Please enter the activity website.")])
  submit = SubmitField('Submit')


class SearchForm(Form):
  age1 = BooleanField('Young Children')
  age2 = BooleanField('Children')
  age3 = BooleanField('Teens')
  age4 = BooleanField('Adults')
  age5 = BooleanField('All Ages')
  price1 = BooleanField('Free')
  price2 = BooleanField('Fee')
  cat1 = BooleanField('Active camps')
  cat2 = BooleanField('Active Games: Equipment Needed')
  cat3 = BooleanField('Active Games: No Equipment Needed')
  cat4 = BooleanField('Aquatics')
  cat5 = BooleanField('Ball Sports')
  cat6 = BooleanField('Dance')
  cat7 = BooleanField('Fitness')
  cat8 = BooleanField('Gymnastics/Tumbling')
  cat9 = BooleanField('Martial Arts')
  cat10 = BooleanField('Mind body')
  cat11 = BooleanField('Playgrounds')
  cat12 = BooleanField('Recreation Spaces')
  cat13 = BooleanField('Trails/Paths')
  submit = SubmitField('Submit')


