# Unit 4: A Unique Social Network (GiveHub)

## Table of Content

1. [Criteria A](#criteria-a)
2. [Criteria B](#criteria-b)
3. [Criteria C](#criteria-c)
4. [Criteria D](#criteria-d)
5. [Citations](#citation)
6. [Appendix](#appendix)

## Criteria A

### Problem Definition

I am a high school student at an International Baccalaureate School and for my Creativity, Activity, and Service project, I am working on improving education in Nepal. I need more funds to invest in my project and have to find alternate sources of funding. I have a limited reach and do not have any means to connect to people beyond my family, friends, and school. I have tried traditional fundraising methods but they have been time-consuming and have proven to be ineffective in securing enough funds. When talking to a friend working on a similar innovative idea, they told me that they couldn't find potential donors and had no way of knowing how many people are interested in their project (See appendix #1 for transcript). Furthermore, there is no way of knowing how many projects/NGOs are in a community and how they are doing that does not violate the privacy of these projects/NGOs.  

I have tried to secure funds by reaching out to family and friends, selling drinks at markets, selling items in garage sales, etc, but these efforts have not been effective in securing enough funds. This method is very time consuming and has a limited reach, which means I am not able to connect with potential donors beyond my immediate network. Additionally, this method does not provide a convenient way for donors to find projects/NGOs that interest them and donate, which discourages them from contributing to the different projects/NGOs.

[See appendix #2 for feedback from advisor on problem definition](#meeting-with-advisor-2-20042023--1433jpt)

### Proposed Solution

My proposed solution is to create an online crowdfunding platform to connect potential donors with projects/NGOs they might be interested in donating to with. I suggest to use Flask as it is a suitable lightweight web framework that is easy to use, flexible, highly customizable, and can be intergrated with several technologies and tools that are rev

Flask is a suitable web framework for building a crowdfunding platform for educational projects and NGOs in Nepal. Flask is a lightweight web framework that is easy to use, flexible, and can be integrated with several technologies and tools that are relevant to the proposed solution.

### Success Criteria

1. __Clear categorization__: The website should clearly categorize charities based on their respective fields, such as education, health, poverty alleviation, and animal welfare, to help users find charities that align with their interests.
2. __Search functionality__: The website should provide a search functionality that allows users to search for charities by name or project name, making it easier to find relevant charities.
3. __Device optimization__: The website should be optimized for all devices, ensuring that users can access and use the site on their smartphones, tablets, and laptops.
4. __Like button__: The website should offer a like button that lets users express their support for a charity and see the number of likes a charity has received.
5. __Charity metrics__: The website should provide charities with measurable metrics, such as the number of likes and number of projects listed, to help them track their performance and make informed decisions.
6. __Site metrics__: The website should provide measurable metrics to the admin regarding the number of charities listed, number of monthly visits, number of projects listed, number of likes in each project.

## Criteria B

### System Diagram

![System Diagram](./img/system_diagram.png)

### Entity Relationship Diagram

![ER Diagram](./img/er_diagram.png)

### Test Plan

|        **Test Cases**       |                          **Purpose**                         |                                             **Inputs**                                            |                                              **Outputs**                                              |
|:---------------------------:|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------:|
|         Login System        |      To ensure login credientials are verified correctly     |      invalid email during registration:   email: 123 username: bob password: @SecurePassword      |                              Verify that the error message is displayed.                              |
|         Login System        |      To ensure login credientials are verified correctly     | valid credentials during regitration: email: bob@gmail.comusername: bob password: @SecurePassword |                  Verify that registration is successful and success message is shown                  |
|         Login System        |      To ensure login credientials are verified correctly     |            Login with incorrect credentials: username: bob password: notsecurepassword            |                                        Verify that login fails                                        |
|         Login System        |      To ensure login credientials are verified correctly     |              Login with correct credentials: username: bob password: @SecurePassword              |                       Verify that login is successful and dashboard can be seen                       |
|  Initial Database Creation  |    To ensure successsful creation of the database tables     |                                                none                                               |                   Verify that tables Charity, Posts, and PostLike have been created                   |
|         Post System         |          To ensure the users can post and view posts         |       try to submit a new post with missing title content: "lorem ipsum" category: "others"       |           Verify that the post was not added to the database and error message was displayed          |
|         Post System         |          To ensure the users can post and view posts         |                      title: "TEST" content: "Test Content" category: "others"                     | Verify that the post was added to the database and is visible in the main page and the dashboard page |
|         Like System         |        To ensure the users can like each other's posts       |                      Click on the like button on the TEST post created above                      |  Verify that the like counter increased and a LikePost instance was created and added to the server.  |
|    Lougout Functionality    | To ensure users can logout and sign into a different account |                          Click on the logout button in the navigation bar                         |          Verify that the user is logged out and removed from the session object in the server         |
| Logged in Privilege Routes  |   To ensure non-logged in users can't view protected routes  |                       Go to all protected endpoints as a non-logged in user                       |                           Ensure the system redirects you to the login page                           |
|    Admin Privilege Routes   |    To ensure non-admin users can't view admin-only routes    |                                        Go to /admin as bob                                        |                                     Ensure the page is not visible                                    |

### Record of Tasks

| **Task No.** |                **Planned Action**                |                               **Planned Outcome**                              | **Time Estimate** | **Target Completion Date** | **Criterion** |
|:------------:|:------------------------------------------------:|:------------------------------------------------------------------------------:|:-----------------:|:--------------------------:|:-------------:|
|       1      |                Meeting with client               |                      Start collecting context for problem                      |       10 min      |        1 April 2023        |       A       |
|       2      |             Create problem defination            |                        Have the client's problem defined                       |       25 min      |        3 April 2023        |       A       |
|       3      |             Create success criterias             | Have the success criteria of the application that solved the client's problems |      1 hours      |        3 April 2023        |       A       |
|       4      |        Present success criteria to advisor       |       Have the success criteria of the application approved by the client      |     10 minutes    |        10 April 2023       |       A       |
|       5      |            Choose suitable CSS Library           |          Have a CSS library to make front end easy to develop and fast         |       1 hour      |       15th April 2023      |       A       |
|       6      |       Write rationale and proposed solution      |         Have the tools used in the application explained and justified         |     45 minutes    |       15th April 2023      |       A       |
|       7      |         Create and explain system diagram        |     Design and explain a system diagram to represent the application system    |     25 minutes    |       15th April 2023      |       B       |
|       8      |          Create Entity Relation Diagram          |              Create and explain relations between database tables              |     20 minutes    |       15th April 2023      |       B       |
|       9      |                Create UML Diagram                |       Create and explain the relation between different classes in python      |     40 minutes    |       15th April 2023      |       B       |
|      10      |      Start working on login system back-end      |          Have a working login system in place (Flask and SQL ALchemy)          |      1 hours      |       25th April 2023      |       C       |
|      11      |             Create WireFrame Diagram             |                 Show how the screens change in the application                 |     30 minutes    |       25th April 2023      |       B       |
|      12      |                   Create Routes                  |    Create all routes necessary in the application including protected routes   |     45 minutes    |       25th April 2023      |       C       |
|      13      |       Create login and register pages HTML       |                        Have the GUI for the login system                       |      2 hours      |       25th April 2023      |       C       |
|      14      |                 Design Test Plan                 |     Design an ellaborate plan for testing the application for possible bugs    |      2 hours      |       25th April 2023      |       B       |
|      15      |                 Create Home page                 |                          Create the landing page GUI                           |      1 hours      |       25th April 2023      |       C       |
|      16      |                Create Posts System               |       Have the user be able to add posts and view posts in dashboard page      |      2 hours      |         1 May 2023         |       C       |
|      17      |                Create Like System                |                      Have the users be able to like a post                     |       1 hour      |         1 May 2023         |       C       |
|      18      | Ensure application succeeds all success criteria |                      Have all success criterias fullfilled                     |       1 hour      |         5 May 2023         |       E       |
|      19      |              Ensure test plan passes             |                    Have all test cases pass to prevent bugs                    |       1 hour      |         5 May 2023         |       E       |
|      20      |            Create video for criteria D           |                     Have a video showcasing the application                    |       1 hour      |        10th Mar 2023       |       D       |
|      21      |              Finish record of tasks              |                        Have a completed record of tasks                        |       1 hour      |        10th Mar 2023       |       C       |
|      22      |              Choose the color theme              |     Experiment color themes and hues and find the best fit for a fridge app    |     20 minutes    |        10th Mar 2023       |       C       |
|      23      |                Complete citations                |                                Finish citations                                |       1 hour      |        10th Mar 2023       |       -       |
|      24      |                  Implimentation                  |                            Implement the Application                           |      30 mins      |         11 May 2023        |       C       |

## Criteria C

### List of Techniques Used

#### Flask Library

#### Object Relational Mapping using SQL Alchemy

##### Creating tables

```.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, or_
from sqlalchemy.sql import func

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    app.root_path, 'database', 'database.db')# initialize the app with the extension

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

```



##### Adding data to tables
##### Retrieving data from tables

#### Coding Principles

##### DRY: Don't Repeat Yourself

I used the DRY Coding principle

#### Git and GitHub

### Development

## Criteria D

## Citation

## Appendix

### Conversation with friend (12/04/2023 @ 18:23JPT)

Purpose: to get information about their project
Outcome: found out they have trouble finding donors

### Meeting with advisor #2 (20/04/2023 @ 14:33JPT)

Purpose: Get problem defintion approved  
Outcome: Problem definition was approved

<https://stackoverflow.com/questions/52665707/how-do-i-implement-a-like-button-function-to-posts-in-python-flask>
