from flask import Flask, session, url_for, request, redirect, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    manager.run()


