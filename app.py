from flask import request
import flask
from flask import Flask
from model import Customer
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SECRET_KEY'] = 'asgk3ltl23'
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def registration():
    form = Customer(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        data = {
            "company_name": request.form['company_name'],
            "item": request.form['item'],
            "count": request.form['count'],
            "price": request.form['price'],
            "mail": request.form['mail'],
            "phone": request.form['phone']
        }
        print(data)
        return 'Спасибо, мы получили ваше предложение, в случае интереса с нашей стороны, мы саяжемся с вами!'
    return flask.render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(threaded=True)