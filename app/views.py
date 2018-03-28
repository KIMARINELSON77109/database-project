"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app,login_manager, db
from flask import render_template, request, redirect, url_for, flash,session,jsonify
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm, SignUpForm
from models import User
from sqlalchemy import create_engine

engine = create_engine('mysql://root:@localhost:3306/ultimate_meal_planner')

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/mealPlan',methods=['GET','POST'])
def mealplan():
    return render_template('meal_plan.html')
    
@app.route('/add_recipe',methods=['GET','POST'])
def add_recipe():
    return render_template('create_recipe.html')
    
@app.route('/signup',methods=['GET' , 'POST'])
def signup():
    form = SignUpForm(csrf_enabled=False)
    
    choices = [(str(x),x) for x in reversed(range(1900,2004))]
    form.D_O_B.choices = choices
    if request.method == 'POST':
        
        if form.validate_on_submit():
            firstname = form.firstname.data
            lastname = form.lastname.data
            D_O_B = form.D_O_B.data
            email = form.email.data
            phone = form.phone.data
            password = form.password.data
            try:
                user = User(firstname,lastname,D_O_B,email,phone,password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('about'))
            except Exception as e:
                print e
                db.session.rollback()
                flash(str(e))
                return render_template('signup.html', form=form)
        else:
            flash('Error signing up')
            render_template('signup.html' , form=form)
    else:
        return render_template('signup.html', form=form)
    
@app.route('/login' , methods=['GET' , 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)

    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            try:
                result = User.query.filter_by(email=email).first()
                print result
                if result is None:
                     flash('Invalid login credentials')
                     return render_template('login.html', form=form)
                else:
                    login_user(result)
                    session['logged_in'] = True
                    flash('You were logged in', 'success')
                    return redirect(url_for('home'))
            except Exception as e:
                return str(e)
        else:
           return render_template('login.html' , form=form)
    else:
        return render_template('login.html', form=form)

@app.route('/measurements',methods=["GET"])
def measurements():
    connection = engine.connect()
    result = connection.execute("select measurement.measurement_name from measurement")
    measurements = []
    for row in result:
        measurements.append(row['measurement_name'])
    connection.close()
    return jsonify({"measurements":measurements})
    
@app.route('/ingredients',methods=["GET"])
def ingredients():
    connection = engine.connect()
    result = connection.execute("select * from ingredient")
    ingredients = []
    for row in result:
        if row['ingredient_id'] != 96:
            ingredients.append(row['ingredient_name'])
    connection.close()
    return jsonify({"ingredients":ingredients})
    
# @app.route('/generate_mealplan',methods=["GET"])
# def newMealPlan():
#     firstconnection = engine.connect()
#     result = firstconnection.execute("select mealplanday.mealplanday_id from mealplanday")
#     mealplandays = []
#     for row in result:
#         mealplandays.append(row['mealplanday_id'])
#     firstconnection.close()
#     return render_template("meal_plan.html")
    
@app.route("/logout")
@login_required
def logout():
    # Logout the user and end the session
    session.pop('logged_in', None)
    flash('You have been logged out.', 'danger')
    return redirect(url_for('about'))    

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
