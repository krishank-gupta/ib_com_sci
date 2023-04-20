from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os 
from markupsafe import escape

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    app.root_path, 'database', 'database.db')# initialize the app with the extension
db.init_app(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String)

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, unique=True, nullable=False)
	desc = db.Column(db.String, nullable=False)

# adding a user
	# u = User(username='admin', email='root')
	# db.session.add(u)
	# db.session.commit()



@app.route("/")
def user_create():
	return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
	message = ''
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		print(username, password)
		message = f"sent to server"
		users = User.query
		for i in users:
			if (i.username) == username:
				message = f"{username} already registered"
	
		return render_template("login.html", message=message)
	else:
		return render_template("login.html", message=message)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

with app.app_context():
	db.create_all()