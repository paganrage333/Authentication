from flask import Flask, redirect, render_template, session
from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG'] = True
app.app_context().push()

connect_db(app)
db.create_all()

@app.route("/")
def root():
    return redirect("/register")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if "username" in session:
        return redirect(f"/users/{session['username']}")
    
    form = RegisterForm()
