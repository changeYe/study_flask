from wtforms import StringField, IntegerField, Form
from wtforms.validators import length, NumberRange, DataRequired


class SearchForm(Form):
    p = StringField(validators=[DataRequired(),length(min=1, max=30,message='错误提示消息')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)],default=1)
