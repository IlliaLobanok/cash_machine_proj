from model import *
from view import login, index
from flask import Flask

app = Flask(__name__, template_folder="template")
app.config["SECRET_KEY"] = "secret key"

app.add_url_rule('/', view_func=index)
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run()
