from random import randint, sample
from faker import Factory
from datetime import date

NUM_USERS = 10
NUM_RECIPES = 10
MEALPLANS= 10
MEALS=35
NUM_INGRED = 50
ingredient_list = """asparagus
apples
avacado
alfalfa
acorn squash
almond
arugala
artichoke
applesauce
asian noodles
antelope
ahi tuna
albacore tuna
Apple juice
Avocado roll
Bruscetta
bacon
black beans
bagels
baked beans
BBQ
bison
barley
beer
bisque
bluefish
bread
broccoli
buritto
babaganoosh
Cabbage
cake
carrots
carne asada
celery
cheese
chicken
catfish
chips
chocolate
chowder
clams
coffee
cookies
corn
cupcakes
crab
curry
cereal
chimichanga
dates
dips
duck
dumplings
donuts
eggs
enchilada
eggrolls
English muffins
edimame
eel sushi
fajita
falafel
fish
franks
fondu
French toast
French dip
Garlic
ginger
gnocchi
goose
granola
grapes
green beans
Guancamole
gumbo
grits
Graham crackers
ham
halibut
hamburger
honey
huenos rancheros
hash browns
hot dogs
haiku roll
hummus
ice cream
Irish stew
Indian food
Italian bread
jambalaya
jelly / jam
jerky
kale
kabobs
ketchup
kiwi
kidney beans
kingfish
lobster
Lamb
Linguine
Lasagna
Meatballs
Moose
Milk
Milkshake
Noodles
Ostrich
Pizza
Pepperoni
Porter
Pancakes
Quesadilla
Quiche
Reuben
Spinach
Spaghetti
Tater tots
Toast
Venison
Waffles
Wine
Walnuts
Yogurt
Ziti
Zucchini"""

recipe_names = """Lemon drizzle cake
Ultimate chocolate cake
Chilli con carne
Yummy scrummy carrot cake
Best-ever brownies
Spiced carrot & lentil soup
Chicken & chorizo jambalaya
Summer-in-winter chicken
Spicy root & lentil casserole
Mustard-stuffed chicken
Classic scones with jam & clotted cream
Red lentil, chickpea & chilli soup
Falafel burgers
Chicken biryani
Raspberry Bakewell cake
Chocolate brownie cake
Classic Victoria sandwich
Creamy courgette lasagne
One-pot chicken chasseur
Unbelievably easy mince pies
Asian Grilled Salmon
Chicken Parmesan
Macaroni and Cheese
Chicken Pot Pie
Chicken Cacciatore
Salisbury Steak
Chocolate Pretzel Peanut Butter Squares
Blackberry Cobbler
Roast Chicken
Sweet and Sour Chicken
Restaurant-Style Salsa
Shrimp Scampi with Linguini
Parmesan-Crusted Pork Chops
Broccoli Cheese Soup
Chicken Tetrazzini
Cheesecake
Roasted Brussels Sprouts
Lemon Ricotta Cookies
Lasagna Rolls
Chicken Tortilla Casserole
Baked Potato Casserole
Baked Penne with Roasted Vegetables
Chicken Spaghetti
Fettuccine Alfredo
Lemon Yogurt Cake
Pot Roast
Guacamole
Chicken-Fried Steak
Tomato Soup
Garlic Roasted Potatoes
Chicken Enchiladas
Roman-Style Chicken
Lemon-Garlic Shrimp and Grits
Chicken Piccata
Beef and Vegetables
Beef Teriyaki
Scrambled Eggs
Egg Casserole
Fish Chowder
Fish and Chips
Mediterranean Fish Cakes
Steamed Tuna Fish
Macadamia Nut Cookies
Pistachio Nut Cake
"""

fake = Factory.create()

BASE_INSERT = "INSERT INTO {} ({}) VALUES({});"

def add_quotes(word):
	return "\"" + word + "\""

def generate_user():
	f = open("db_data.sql", "w")
	table = "user"
	fields = ['firstname','lastname', 'D_O_B','email', 'phone','password']
	for x in range(NUM_USERS):
		fake.seed(x)
		vals = [add_quotes(fake.first_name()), add_quotes(fake.last_name()), add_quotes(fake.date()),add_quotes(fake.email()), add_quotes(fake.phone_number()), add_quotes("password123")]

		f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
	f.close()
def generate_profile():
        f = open("db_data.sql", "a+")
        table = "profile"
        fields = ['user_id','profile_id','diet_type']
        diets = ["Classic","Vegetarian","Vegan","Diabetic"]
        for x in range(1,NUM_USERS-1):
                diet = str(diets[randint(0,3)])
                vals = [str(x),str(x),add_quotes(diet)]
                f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
        f.close()             
                
def generate_recipe():
	f = open("db_data.sql", "a+")
	table = "recipe"
	fields = ["recipe_name", "recipe_picture", "prep_time","cook_time", "servings", "diet_type"]
	image = add_quotes("Kimari Nelson_2018-04-04-03-59-45_pexels-photo-247685.png")
	diets = ["Classic","Vegetarian","Vegan","Diabetic"]
	recipes = recipe_names.split("\n")
	for x in range(1,NUM_RECIPES + 1):
		preptime = str(randint(10, 60))+" "+"Minutes"
		cooktime = str(randint(10, 120))+" "+"Minutes"
		serving = str(randint(1,5))
		diet = str(diets[randint(0,3)])
		recipe = add_quotes(recipes[randint(1,50)])
		vals = [recipe,image, add_quotes(preptime),add_quotes(cooktime),serving,add_quotes(diet)]
		f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
	f.close()

def generate_ingr_rec():
	f = open("db_data.sql", "a+")
	table = "needs"
	fields = ["ingredient_id", "recipe_id","measurement_id", "quantity"]
	for x in range(1, NUM_RECIPES + 1):
		ingrs = randint(3,4)
		used = set([])
		rec_used = set([])
		for y in range(ingrs):
			meas = randint(1,9)
			quantity = randint(1,10)
			while True:
				ingr = randint(1,120)
				if ingr in used and x in rec_used:
					continue
				else:
					vals = [str(ingr), str(x), str(meas), str(quantity)]
					used.add(ingr)
					rec_used.add(x)
					f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
					break
	f.close()

def generate_ingr():
	f = open("db_data.sql", "a+")
	table = "ingredients"
	fields = ['ingredient_name']
	ingredients = ingredient_list.split("\n")
	for x in range(len(ingredients)):
		vals = [add_quotes(ingredients[x])]
		f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
	f.close()

def generate_instr():
   verbs = ['Add', 'slice', 'season', 'rub', 'cut']

   ingredients = ingredient_list.split("\n")
   table = "instruction"
   fields = ["recipe_id","step_num","direction"]
   instruction_format = "{} the {}"
   f = open("db_data.sql", "a+")
   for x in range(1, NUM_RECIPES + 1):
                num_instr = randint(4,5)
                instruction = []
                for y in range(num_instr):
                        for ingredient in ingredients:
                                instruction.append(add_quotes(instruction_format.format(verbs[randint(0,4)], ingredient)))
                        instru = str(instruction[randint(0,120)])
                        vals = [str(x),str(y+1),instru]
                        f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
   f.close()
def add_recipe():
        table = "add_recipe"
        fields = ["user_id","recipe_id","date_created"]
        f = open("db_data.sql", "a+")
        for x in range(1, NUM_RECIPES + 1):
                user = randint(1, NUM_USERS)
                year = 2018
                month = randint(1, 12)
                day = randint(1, 28)
                date_add = date(year, month, day)
                vals = [str(user),str(x),str(date_add)]
                f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
        f.close()

def generate_makes():
        table = "makes"
        fields = ["meal_id","recipe_id"]
        f = open("db_data.sql", "a+")
        for x in range(1, MEALS):
                rec = randint(1, NUM_RECIPES)
                vals = [str(x),str(rec)]
                f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
        f.close()
                
def generate_meal():
	recipes = recipe_names.split("\n")
	f = open("db_data.sql","a+")
	table = "meal"
	fields = ["meal_name","meal_type","num_calorie"]
	types = ["Breakfast", "Lunch", "Dinner"]
	for x in range(0,MEALS-1):
		name = add_quotes(recipes[x].strip())
		mealtype = add_quotes(types[randint(0,2)])
		calories = str(randint(250, 2000))
		vals = [name,mealtype,calories]
		f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
	f.close()
def generate_mealplan():
        f = open("db_data.sql","a+")
        table = "meal_plan"
        fields = ["mealplan_id","end_date"]
        for x in range(1,MEALPLANS):
                year = 2018
                month = randint(1, 12)
                day = randint(1, 28)
                end_date = date(year, month, day)
                vals = [str(x),str(end_date)]
                f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
        f.close()
	
def generate_planmeal():
	f = open("db_data.sql","a+")
	table = "contains"
	fields =["mealplan_id","meal_id"]
	for x in range(1,MEALPLANS):
		mealplandays = randint(1,MEALS)
		for y in range(mealplandays):
			vals = [str(x),str(mealplandays)]
			f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
			break
	f.close()
	
def generate_kitchen():
   f = open("db_data.sql", "a+")
   table = "kitchen"
   fields = [ "user_id","ingredient_id","quantity"]
   for x in range(1,6):
                for x in range(1, NUM_USERS):
                        quan = randint(2,9)
                        ingrd = randint(1,NUM_INGRED)
                        vals = [str(x), str(ingrd),str(quan)]
                        f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
   f.close()
# to do ---  profile, makes
generate_user()
generate_profile()
generate_recipe()
generate_ingr()
generate_ingr_rec()
add_recipe()
generate_instr()
generate_meal()
generate_makes()
generate_mealplan()
generate_planmeal()
generate_kitchen()


