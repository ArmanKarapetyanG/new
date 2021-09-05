from wtforms import SubmitField, StringField, PasswordField, validators, IntegerField
from flask_wtf import Form
class Customer(Form):
  company_name = StringField('Название Компании / ИП',
                 [validators.DataRequired()])
  item = StringField('Товар или услуга',
                 [validators.DataRequired()])
  count = IntegerField('Количество или время в часах, если это услуга', [validators.DataRequired()])
  price = IntegerField('Цена за единицу товара или за час работы', [validators.DataRequired()])
  mail = StringField('Ваша почта', [validators.DataRequired(), validators.Email()])
  phone = IntegerField('Телефон (8**********)',
                 [validators.DataRequired()])
  submit = SubmitField('Отправить')