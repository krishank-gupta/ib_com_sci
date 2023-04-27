from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os 
# from markupsafe import escape
from static.library import hash_password, check_password

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    app.root_path, 'database', 'database.db')# initialize the app with the extension
db.init_app(app)

class Charity(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, unique=True, nullable=False)
	desc = db.Column(db.String, nullable=False)

@app.route("/")
def index():
	return render_template("landing.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	message = ''
	if request.method == 'POST':
		signup_email = request.form['signup_email']
		signup_username = request.form['signup_username']
		signup_password = hash_password(request.form['signup_password'])
		print(signup_email, signup_username, signup_password)
		u = Charity(email=signup_email, username=signup_username, password=signup_password)
		db.session.add(u)
		db.session.commit()
		message = f"Registration Success. Proceed to Login."
		return render_template("signup.html", message=message)
	else:
		return render_template("signup.html", message=message)
	
@app.route("/login", methods=['GET', 'POST'])
def login():
	message = ''
	error = ''
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		charities = Charity.query.all()
		for charity in charities:
			if charity.username == username and check_password(password, charity.password):
				message = "success"
				return redirect(url_for('show_user_profile', username=username))
			else:
				message = "error"
				error = True
		return render_template("login.html", message=message, error=error)
	else:
		return render_template("login.html", message=message, error=error)
	
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return render_template('dashboard.html', username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

with app.app_context():
	db.create_all()