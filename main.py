from model import *
from view import *
from flask import Flask

app = Flask(__name__, template_folder="template")
app.config["SECRET_KEY"] = "secret key"

app.add_url_rule('/', view_func=index)
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/cashier', view_func=index_cashier, methods=['GET', 'POST'])
app.add_url_rule('/open_receipt', view_func=open_receipt, methods=['GET', 'POST'])
app.add_url_rule('/add_product', view_func=add_product, methods=['POST'])
app.add_url_rule('/close_receipt', view_func=close_receipt)

if __name__ == '__main__':
    app.run()
