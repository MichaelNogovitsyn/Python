from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired

class Lf(FlaskForm):
    name = StringField("имя", validators = [DataRequired])
    email = EmailField("почта", validators = [DataRequired])
    password = PasswordField("пароль", validators = [DataRequired])
    password_again = PasswordField("пароль повтор", validators = [DataRequired])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироватся')