"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import time
from app import app,login_manager, db, ALLOWED_EXTENSIONS
from flask import render_template, request, redirect, url_for, flash,session,jsonify
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm, SignUpForm,RecipeForm,GenPlanForm
from models import User
from sqlalchemy import create_engine
from werkzeug import secure_filename

engine = create_engine('mysql://root:@localhost:3306/ultimate_meal_planner')

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
@app.route('/viewMeal/')
def viewMeal():
    """Render website's home page."""
    return render_template('viewMeal.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/generateMealPlan',methods=['GET','POST'])
def GenMealPlan():
    form = GenPlanForm(csrf_enabled=False)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            calorie = form.calorie.data
            return redirect(url_for(''))
    return render_template('gen_meal_plan.html',form=form)
    
#-------------------------------------------------------------------------------
#                           SIGN UP
#-------------------------------------------------------------------------------
@app.route('/signup',methods=['GET' , 'POST'])
def signup():
    form = SignUpForm(csrf_enabled=False)
    
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
 
#-------------------------------------------------------------------------------
#                           LOGIN
#-------------------------------------------------------------------------------  
@app.route('/login' , methods=['GET' , 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)

    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            try:
                result = User.query.filter_by(Password=password).first()
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

#-------------------------------------------------------------------------------
#                           ADD RECIPE
#------------------------------------------------------------------------------- 
@app.route('/add_recipe',methods=['GET','POST'])
def add_recipe():
    form = RecipeForm(request.form)
    if request.method=="POST":
        uploadedfile = request.files['uploadedfile']
        if uploadedfile and allowed_file(uploadedfile.filename):
            uploadedfilename = form.name.data + '_' + str(time.strftime("%Y-%m-%d-%H-%M-%S")) + "_" + secure_filename(uploadedfile.filename)
            filepath = os.path.join(os.getcwd() + '/app/static/recipeImages/',uploadedfilename)
            uploadedfile.save(filepath)
        connection = engine.raw_connection()
        cursor = connection.cursor()
        cursor.callproc("AddRecipe", [str(form.name.data),str(uploadedfilename),str(form.preptime.data),str(form.cooktime.data),str(form.serving.data)])
        result = cursor.fetchall()
        cursor.close()
        connection.commit()
        firstconnection = engine.connect()
        result = firstconnection.execute("SELECT MAX(recipe_id) FROM recipe LIMIT 1;")
        for row in result:
            iidd = row['MAX(recipe_id)']
        print iidd
        firstconnection.close()
        return redirect(url_for('recipes'))
    else:
        return render_template('create_recipe.html',form=form)
        
#-------------------------------------------------------------------------------
#                           VIEW ALL RECIPES
#-------------------------------------------------------------------------------          
@app.route('/recipes', methods=["GET"])
def recipes():
    connection = engine.connect()
    result = connection.execute("select * from recipe")
    recipess = []
    for row in result:
        recipess.append(row)
    recipes = [{"recipe_id":recipe.recipe_id,"recipe_name": recipe.recipe_name, "recipe_picture": recipe.recipe_picture, "prep_time": recipe.prep_time, "cook_time": recipe.cook_time,"servings":recipe.servings} for recipe in recipess]
    if request.method == 'GET':
        if result is not None:
            return render_template("recipes.html", recipes=recipess)
    else:
        return redirect(url_for("home"))

#-------------------------------------------------------------------------------
#            GET MEASUREMENTS FROM DB AND SENDS JSON OBJECT TO RECIPE FORM
#------------------------------------------------------------------------------- 
@app.route('/measurements',methods=["GET"])
def measurements():
    connection = engine.connect()
    result = connection.execute("select measurement.measurement_name from measurement")
    print result
    measurements = []
    for row in result:
        measurements.append(row['measurement_name'])
    connection.close()
    return jsonify({"measurements":measurements})

#-------------------------------------------------------------------------------
#            GET INGREDIENTS FROM DB AND SENDS JSON OBJECT TO RECIPE FORM
#-------------------------------------------------------------------------------     
@app.route('/ingredients',methods=["GET"])
def ingredients():
    connection = engine.connect()
    result = connection.execute("select * from ingredients")
    ingredients = []
    for row in result:
        if row['ingredient_id'] != 96:
            ingredients.append(row['ingredient_name'])
    connection.close()
    return jsonify({"ingredients":ingredients})

#-------------------------------------------------------------------------------
#            VIEW DETAILS OF INDIVIDUAL RECIPES
#------------------------------------------------------------------------------- 
@app.route('/recipedetails/<recipeid>',methods=["GET"])
def recipedetails(recipeid):
    connection = engine.raw_connection()
    cursor = connection.cursor()
    cursor.callproc("GetRecipeById",[str(recipeid)])
    result = cursor.fetchall()
    cursor.close()
    cursor = connection.cursor()
    cursor.callproc("recipeinstruction",[str(recipeid)])
    result_instr = cursor.fetchall()
    cursor.close()
    cursor = connection.cursor()
    cursor.callproc("GetIngrMeasurFromRecipe",[str(recipeid)])
    result_ingred = cursor.fetchall()
    cursor.close()
    connection.commit()
    ingred = []
    recipes = []
    instr = []
    for row in result:
        recipes.append(row)
    for row in result_instr:
        instr.append(row)
    for row in result_ingred:
        ingred.append(row)
    return render_template("recipe.html",recipes=recipes, instrs=instr,ingreds=ingred)
    
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

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

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
