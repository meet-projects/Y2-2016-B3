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
		new_email = request.form["email"]
		new_country = request.form["country"]
		new_gender = request.form["sex"]
		new_password = request.form["password"]
		new_dob = request.form["dob"]

		new_user = Users(
			fullname=new_name,
			email=new_email,
			country=new_country,
			gender=new_gender,
			password=new_password,
			dob=new_dob
			)

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

@app.route('/profile/<int:friend_id>')
def otherprofile(friend_id):
	print(friend_id)
	if 'user_email' in flask_session:
		loggeduser = session.query(Users).filter_by(email=flask_session['user_email']).first()
		otheruser = session.query(Users).filter_by(id = friend_id).first()
		return render_template('UserProfile.html', user=otheruser)
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



@app.route('/country/<int:country_id>/',  methods=['GET', 'POST'])
def countryprofile(country_id):	
	if 'user_email' in flask_session:
		user = session.query(Users).filter_by(email=flask_session['user_email']).first()
		country=session.query(Country).filter_by(id=country_id).first()
		getposts = session.query(Post).filter_by(country_id=country_id).all()
		getposts.reverse()
		if request.method == 'GET':
			return render_template('countryprofile.html',country=country, user=user , posts = getposts)
		else :
			new_content = request.form["content"]
			new_post = Post(
				content = new_content,
				country_id=country.id,
				user_id = user.id
				)
			session.add(new_post)
			session.commit()

			getposts = session.query(Post).filter_by(country_id=country_id).all()
			getposts.reverse()
			print(getposts[0].content)
			return redirect(url_for('countryprofile',country_id=country.id, posts=getposts))
	else:
		return redirect(url_for('gotosignin'))

@app.route('/logout')
def logout():
	flask_session.pop('user_email', None)
	return redirect(url_for('homepage'))


'''
@app.route('/add/<int:country_id>/', methods=['GET', 'POST'])
def add(country_id):
	if 'user_email' in flask_session:
		get_country=session.query(Country).filter_by(id=country_id).first()
		user = session.query(Users).filter_by(email=flask_session['user_email']).first()
		if request.method == 'GET':
			return render_template('countryprofile.html', country_id=country_id)
		elif request.method == 'POST':
			new_content = request.form["content"]
			new_post = Post(
				content = new_content,
				country_id=get_country.id,
				user_id = user.id
				)
			session.add(new_post)
			session.commit()

			getposts = session.query(Post).filter_by(country_id=country_id).all()
			getposts.reverse()
			return redirect(url_for('countryprofile', country_id=country_id,country=get_country, posts=getposts))
	else:
		return redirect(url_for('gotosignin'))
'''



app.secret_key = '38087xsx9c70saeu0rq'
if __name__ == '__main__':
    app.run(debug=True)
