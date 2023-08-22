import random
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

def pw_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_let = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pw_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pw_num = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = pw_sym + pw_let + pw_num

    random.shuffle(password_list)
    password = "".join(password_list)

    # pyperclip.copy(password)


class RegistrationForm(FlaskForm):

    username = StringField(label="Username", validators=[DataRequired(), Length(min=6, max=12)])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=12, max=18)])
    confirmPassword = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=12, max=18)])
    submit = SubmitField("Login")

import random
import pyperclip
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

def pw_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_let = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pw_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pw_num = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = pw_sym + pw_let + pw_num

    random.shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)


class RegistrationForm(FlaskForm):

    username = StringField(label="Username", validators=[DataRequired(), Length(min=6, max=12)])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=12, max=18)])
    confirmPassword = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=12, max=18)])
    submit = SubmitField("Login")

