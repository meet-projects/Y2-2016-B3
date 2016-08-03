from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE

@app.route('/')
def homepage():
	return render_template('homepage.html')


@app.route('/signup')
def gotosignup():
	return render_template('signup.html')


@app.route('/signin')
def gotosignin():
	return render_template('signin.html')

@app.route('/map')
def map():
	return render_template('map.html')

@app.route('/country')
def countryprofile():
	return render_template('countryprofile.html')

if __name__ == '__main__':
    app.run(debug=True)
