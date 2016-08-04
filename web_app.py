from flask import Flask, render_template, request, redirect, url_for
from flask import session as flask_session
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base, Users, Country, Post

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


@app.route('/signup', methods=['GET', 'POST'])
def gotosignup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		new_name = request.form["fullname"]
		print('A')
		new_email = request.form["email"]
		print('B')
		new_country = request.form["country"]
		print('C')
		new_gender = request.form["sex"]
		print('D')
		new_password = request.form["password"]
		print('E')
		new_dob = request.form["dob"]
		print('F')

		new_user = Users(
			fullname=new_name,
			email=new_email,
			country=new_country,
			gender=new_gender,
			password=new_password,
			dob=new_dob
			)
		print('G')

		session.add(new_user)
		session.commit()
		flask_session['user_email'] = new_email
		return redirect(url_for('userprofile'))




@app.route('/userprofile')
def userprofile():
	if 'user_email' in flask_session:
		user = session.query(Users).filter_by(email=flask_session['user_email']).first()
		return render_template('UserProfile.html', user=user)
	else:
		return redirect(url_for('gotosignin'))


@app.route('/signin', methods=['GET', 'POST'])
def gotosignin():
	if request.method == 'GET':
		return render_template('signin.html')
	else:
		new_email = request.form['email']
		new_password = request.form['password']

		users = session.query(Users).filter_by(email = new_email, password=new_password).all()
		if(len(users) == 0):
			return redirect(url_for('gotosignin'))
		else:
			flask_session['user_email'] = new_email
			return redirect(url_for('userprofile'))

@app.route('/map')
def map():
	countries=session.query(Country).all()
	return render_template('map.html', countries=countries)

@app.route('/country/<int:country_id>/')
def countryprofile(country_id):	
	if 'user_email' in flask_session:
		user = session.query(Users).filter_by(email=flask_session['user_email']).first()
		country=session.query(Country).filter_by(id=country_id).first()
		return render_template('countryprofile.html', user=user, country=country)
	else:
		return redirect(url_for('gotosignin'))
@app.route('/logout')
def logout():
	flask_session.pop('user_email', None)
	return redirect(url_for('homepage'))  

@app.route('/add/<int:country_id>/', methods=['GET', 'POST'])
def add(country_id):
	if request.method == 'GET':
		return render_template('addpost.html', country_id=country_id)
	elif request.method == 'POST':
		if 'user_email' in flask_session:
			user = session.query(Users).filter_by(email=flask_session['user_email']).first()
			country=session.query(Country).filter_by(id=country_id).first()
			new_content = request.form["content"]
			new_post = Post(
				content = new_content,
				country_id=country.id,
				user_id = user.id
				)
			session.add(new_post)
			session.commit()

			return render_template('countryprofile.html', country_id=country_id)
	else:
		return redirect(url_for('gotosignin'))




app.secret_key = '38087xsx9c70saeu0rq'
if __name__ == '__main__':
    app.run(debug=True)
