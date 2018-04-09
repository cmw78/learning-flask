from flask import Flask, render_template, request, session, redirect, url_for
import models
from models import db, User, Place, activitydata
from forms import SignupForm, LoginForm, AddressForm, ActivityForm, SearchForm, ActivityForm2
import requests
import json
from sqlalchemy import or_
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)
app.secret_key = "development-key"

@app.route('/activities')
def all_activities():
  activities = db.session.query(models.activitydata).all()
  return render_template('view-activities.html', activities=activities)

@app.route('/activity/<name>')
def see_activity(name):
    activity = db.session.query(models.activitydata)\
        .filter(models.activitydata.name== name).one()
    return render_template('see-activity.html', activity=activity)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/homepage")
def homepage():
  return render_template("homepage.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
    return redirect(url_for('home'))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      return redirect(url_for('homepage'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)


@app.route("/add2", methods=["GET", "POST"])
def addActivity2():
  form = ActivityForm2()
  if request.method == "POST":
    if form.validate() == False:
      return render_template('add-activity.html', form=form)
    else:
      age = 'none'
      cat = 'none'
      price = 'none'

      if form.age1.data == True:
        age = 'young children'
      elif form.age2.data == True:
        age = 'children'
      elif form.age3.data == True:
        age = 'teens'
      elif form.age4.data == True:
        age = 'adults'
      elif form.age5.data == True:
        age = 'all ages'
      if form.price1.data == True:
        price = 'free'
      elif form.price2.data == True:
        price = 'fee'

      if form.cat1.data == True:
        cat = 'active camps'
      elif form.cat2.data == True:
        cat = 'active games: equipment needed'
      elif form.cat3.data == True:
        cat = 'active games: no equipment needed'
      elif form.cat4.data == True:
        cat = 'aquatics'
      elif form.cat5.data == True:
        cat = 'ball sports'
      elif form.cat6.data == True:
        cat = 'dance'
      elif form.cat7.data == True:
        cat = 'fitness'
      elif form.cat8.data == True:
        cat = 'gymnastics/tumbling'
      elif form.cat9.data == True:
        cat = 'martial arts'
      elif form.cat10.data == True:
        cat = 'mind body'
      elif form.cat11.data == True:
        cat = 'playgrounds'
      elif form.cat12.data == True:
        cat = 'recreation spaces'
      elif form.cat13.data == True:
        cat = 'trails/paths'

      newAct = activitydata(form.name.data, form.address.data, form.description.data, age, price, cat, form.website.data)
      db.session.add(newAct)
      db.session.commit()

      return redirect(url_for('homepage'))

  elif request.method == "GET":
    return render_template('add-activity.html', form=form)
@app.route("/search", methods=["GET", "POST"])
def search():
  form = SearchForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('search-form.html', form=form)
    else:
      filtAge= False
      filtPrice = False
      filtCat = False

      agelist = []
      catlist = []
      pricelist = []
      if form.age1.data == True:
        age = 'young children'
        agelist.append(age)
        filtAge = True
      if form.age2.data == True:
        age = 'children'
        agelist.append(age)

        filtAge=True
      if form.age3.data == True:
        age = 'teens'
        agelist.append(age)

        filtAge = True
      if form.age4.data == True:
        age = 'adults'
        agelist.append(age)

        filtAge = True

      if form.age5.data == True:
        age = 'all ages'
        agelist.append(age)

        filtAge = True

      if form.price1.data == True:
        price = 'free'
        pricelist.append(price)
        filtPrice = True
      if form.price2.data == True:
        price = 'fee'
        pricelist.append(price)
        filtPrice = True
      if form.cat1.data == True:
        cat = 'active camps'
        catlist.append(cat)
        filtCat = True
      if form.cat2.data == True:
        cat = 'active games: equipment needed'
        catlist.append(cat)

        filtCat = True
      if form.cat3.data == True:
        cat = 'active games: no equipment needed'
        catlist.append(cat)

        filtCat = True
      if form.cat4.data == True:
        cat = 'aquatics'
        catlist.append(cat)

        filtCat = True
      if form.cat5.data == True:
        cat = 'ball sports'
        catlist.append(cat)
        filtCat = True
      if form.cat6.data == True:
        cat = 'dance'
        catlist.append(cat)
        filtCat = True
      if form.cat7.data == True:
        cat = 'fitness'
        catlist.append(cat)
        filtCat = True
      if form.cat8.data == True:
        cat = 'gymnastics/tumbling'
        catlist.append(cat)
        filtCat = True
      if form.cat9.data == True:
        cat = 'martial arts'
        catlist.append(cat)
        filtCat = True
      if form.cat10.data == True:
        cat = 'mind body'
        catlist.append(cat)
        filtCat = True
      if form.cat11.data == True:
        cat = 'playgrounds'
        catlist.append(cat)

        filtCat = True
      if form.cat12.data == True:
        cat = 'recreation spaces'
        catlist.append(cat)
        filtCat = True
      if form.cat13.data == True:
        cat = 'trails/paths'
        catlist.append(cat)
        filtCat = True

      #if form.age1.data==True or form.age2.data==True or form.age3.data==True or form.age4.data==True or form.age5.data:
        #filtAge = True
      #if form.price1.data or form.price2.data
        #filtPrice = True
      #if form.cat1.data or form.cat2.data or form.cat3.data or form.cat4.data or form.cat5.data or form.cat6.data or form.cat7.data or form.cat8.data or form.cat9.data or form.cat10.data or form.cat11.data or form.cat12.data or form.cat13.data:
        #filtCat = True
      if filtAge==True and filtPrice==False and filtCat==False:
        activities = db.session.query(models.activitydata)\
          .filter((or_(models.activitydata.age==v for v in agelist)))
      elif filtAge==False and filtPrice==True and filtCat==False:
        activities = db.session.query(models.activitydata)\
          .filter((or_(models.activitydata.fee==v for v in pricelist)))
      elif filtAge==False and filtPrice==False and filtCat==True:
        activities = db.session.query(models.activitydata)\
          .filter((or_(models.activitydata.category==v for v in catlist)))
      elif filtAge==True and filtPrice==True and filtCat==False:
        activities = db.session.query(models.activitydata)\
          .filter((or_(models.activitydata.fee==v for v in pricelist)))\
          .filter((or_(models.activitydata.age==v for v in agelist)))
      elif filtAge==True and filtPrice==False and filtCat==True:
        activities = db.session.query(models.activitydata)\
          .filter((or_(models.activitydata.age==v for v in agelist)))\
          .filter((or_(models.activitydata.category==v for v in catlist)))
      elif filtAge==False and filtPrice==True and filtCat==True:
        activities = db.session.query(models.activitydata)\
          .filter((or_(models.activitydata.fee==v for v in pricelist)))\
          .filter((or_(models.activitydata.category==v for v in catlist)))
      elif filtAge==True and filtPrice==True and filtCat==True:
        activities = db.session.query(models.activitydata)\
          .filter((or_(models.activitydata.age==v for v in agelist)))\
          .filter((or_(models.activitydata.fee==v for v in pricelist)))\
          .filter((or_(models.activitydata.category==v for v in catlist)))
      return render_template('all-activities.html', activities=activities)

      #session['email'] = newuser.email
      #return redirect(url_for('list', activities=activities))

  elif request.method == "GET":
    return render_template('search-form.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('homepage'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data 
      password = form.password.data 

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data 
        return redirect(url_for('homepage'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))

@app.route("/home", methods=["GET", "POST"])
def home():
  if 'email' not in session:
    return redirect(url_for('login'))

  form = AddressForm()
  places = []
  my_coordinates = (37.4221, -122.0844)

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('home.html', form=form)
    else:
      # get the address
      address = form.address.data 
      #address = add

      # query for places around it
      p = Place()
      my_coordinates = p.address_to_latlng(address)
      places = p.query(address)

      # return those results
      return render_template('home.html', form=form, my_coordinates=my_coordinates, places=places)

  elif request.method == 'GET':
    return render_template("home.html", form=form, my_coordinates=my_coordinates, places=places)

if __name__ == "__main__":
  app.run()