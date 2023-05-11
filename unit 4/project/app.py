from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, or_
from sqlalchemy.sql import func
import os 
# from markupsafe import escape
from static.library import hash_password, check_password
from datetime import datetime

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
adminUsername = "sys_admin"

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    app.root_path, 'database', 'database.db')# initialize the app with the extension
app.secret_key = os.urandom(12)
db.init_app(app)

class Charity(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, unique=True, nullable=False)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, unique=False, nullable=False)
	posts = db.relationship('Posts', backref='author', lazy='dynamic')

	def like_post(self, post):
		if not self.has_liked_post(post):
			like = PostLike(user_id=self.id, post_id=post.id)
			db.session.add(like)
			db.session.commit()
		else:
			PostLike.query.filter_by(
				user_id=self.id,
				post_id=post.id).delete()
			db.session.commit()


	def has_liked_post(self, post):
		return PostLike.query.filter(
			PostLike.user_id == self.id,
			PostLike.post_id == post.id).count() > 0

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('charity.id'))
	title = db.Column(db.String(1000), nullable=False) # Added this line
	content = db.Column(db.String(1000), nullable=False)
	category = db.Column(db.String(1000), nullable=False)
	timestamp = db.Column(DateTime(timezone=True), default=func.now())
	likes = db.relationship('PostLike', backref='post', lazy='dynamic')

	def get_like_count(self):
		return self.likes.count()

class PostLike(db.Model):
	__tablename__ = 'post_like'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('charity.id'), nullable=False)
	post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)


# Define a custom decorator to check if the user is logged in
def login_required(f):
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

def admin_privilege_required(f):
	def wrapper(*args, **kwargs):
		# print(session['username'])
		if 'username' not in session or session['username'] != adminUsername:
			return redirect(url_for('index'))
		return f(*args, **kwargs)
	wrapper.__name__ = f.__name__
	return wrapper

@app.route("/", methods=['GET','POST'])
def index():
	data = []
	
	if request.method == 'POST':
		category = request.form['category']
		if not (category == "all"):
			posts = Posts.query.filter_by(category=category).all()
			for p in posts:
				data.append((p.id, p.author.username, p.title, p.content, p.category, p.timestamp, p.get_like_count()))
			return render_template("landing.html", data=data, category=category)
		else:
			posts = Posts.query.all()
			for p in posts:
				data.append((p.id, p.author.username, p.title, p.content, p.category, p.timestamp, p.get_like_count()))
			return render_template("landing.html", data=data)
	else:
		posts = Posts.query.all()
		for p in posts:
			data.append((p.id, p.author.username, p.title, p.content, p.category, p.timestamp, p.get_like_count()))
		return render_template("landing.html", data=data)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	message = ''
	if request.method == 'POST':
		signup_email = request.form['signup_email']
		signup_username = request.form['signup_username']
		signup_password = hash_password(request.form['signup_password'])
		# print(signup_email, signup_username, signup_password)
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
				session['username'] = username
				return redirect(url_for('show_user_profile'))
			else:
				message = "error"
				error = True
		return render_template("login.html", message=message, error=error)
	else:
		return render_template("login.html", message=message, error=error)
	
@app.route('/dashboard')
@login_required
def show_user_profile():
    # show the user profile for that user
	# data =  []
	# posts = Posts.query.all()
	# for p in posts:
	# 	data.append((p.id, p.author.username, p.title, p.get_like_count()))
	# print(data)
	current_user = session.get('username')
	user = Charity.query.filter_by(username=current_user).first()
	posts = user.posts.all()
	print(posts)
	return render_template('dashboard.html', data=posts)

@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
	if request.method == 'POST':
		username = session.get('username')
		title = request.form['title']
		content = request.form['content']
		category = request.form['category']
		user = Charity.query.filter_by(username=username).first()
		p = Posts(title=title, author=user, content=content, category=category)
		db.session.add(p)
		db.session.commit()
		return render_template('add_post.html')
	else:
		return render_template('add_post.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
	p = Posts.query.filter_by(id=post_id).first()
	return f'({p.id}, {p.author.username}, {p.title}, {p.content}, {p.category}, {p.timestamp}, {p.get_like_count()})'

@app.route('/like', methods=['POST'])
@login_required
def like_post():
	post_id = request.form['post_id']
	post = Posts.query.filter_by(id=post_id).first_or_404()
	current_user = session.get('username')
	user = Charity.query.filter_by(username=current_user).first()
	print(user.id, post.id)
	user.like_post(post)


	return redirect(request.referrer)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/search')
def search():
	data = []
	query = request.args.get('query')
	posts = Posts.query.filter(or_(Posts.title.contains(query), Posts.content.contains(query))).all()
	for p in posts:
		data.append((p.id, p.author.username, p.title, p.content, p.category, p.timestamp, p.get_like_count()))
	return render_template('search-results.html', data=data)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/admin')
@admin_privilege_required
def admin():
	user_data = []
	post_data = []
	users = Charity.query.all()
	for user in users:
		user_data.append(f"username: {user.username}, id: {user.id}")
	posts = Posts.query.all()
	for p in posts:
		post_data.append((p.id, p.author.username, p.title, p.content, p.category, p.timestamp, p.get_like_count()))
	print(post_data)
	return render_template('admin.html', users=user_data, post_data=post_data)

with app.app_context():
	db.create_all()