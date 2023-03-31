from flask import Flask, render_template, request
# Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, delete

Base = declarative_base()

# create table
class users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(300))

    def __repr__(self) -> str:
        return f"""id: {self.id},email: {self.email},username: {self.username},password: {self.password}"""

class posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    content = Column(String(250),nullable=False)
    img = Column(String(300), nullable=False)
    date = Column(String, nullable=False)
    user_id = Column(String(300), nullable=False)

    def __repr__(self) -> str:
        return f"""{self.id}, {self.title}, {self.content}, {self.img}, {self.date}, {self.user}"""

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)
Base.metadata.bind = engine

session = sessionmaker(bind=engine)
database_session = session()

# Simple Select all users query using SQL Alchemy
# query = select(users)
# res = database_session.execute(query).fetchall()
# print(res)

# Routes
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/requests", methods=["GET", "POST"])
def requests():
    result = ""
    result2 = ""

    if request.method == "GET":
        # currency converter
        usd_value = request.args.get("usd_value")
        if usd_value:
            jpy = int(usd_value) * 132
            result = f"{usd_value} USD is: {jpy:.2f} JPY"

    elif request.method == "POST":
        # password chcek
        check_pass = request.form["check_pass"]
        if check_pass:
            if len(check_pass) > 8:
                result2="Your password is safe"
            else:
                result2="Not safe"
        
    return render_template("requests.html", data=result, data2=result2)



if __name__ == '__main__':
    app.run()
