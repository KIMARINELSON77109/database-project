from random import randint, sample
from faker import Factory

NUM_USERS = 500000
NUM_RECIPES = 1000000


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
breadcrums
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
jalapeño
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


def generate_user(num):
	f = open("db_data.sql", "w")
	table = "user"
	fields = ['firstname', 'lastname', 'D_O_B', 'email,','phone','user_password']
	for x in range(num):
		fake.seed(x)
		vals = [add_quotes(fake.first_name()), add_quotes(fake.last_name()), add_quotes(fake.date()),add_quotes(fake.email()), add_quotes(fake.phone_number()), add_quotes("password")]

		f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
	f.close()

def generate_ingr():
	f = open("db_data.sql", "a+")
	table = "ingredient"
	fields = ['ingredient_name', 'food_group']
	types = ['nuts', 'dairy', 'pork', 'beef', 'wheat','Carbs','Friut','Fats']
	ingredients = ingredient_list.split("\n")
	for x in range(len(ingredients)):
		vals = [add_quotes(ingredients[x]), add_quotes(types[randint(0,12)])]
		f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
	f.close()



def generate_recipe():
	f = open("db_data.sql", "a+")
	table = "recipe"
	fields = ["recipe_name", "recipe_picture", "prep_time","cook_time", "servings", "diet_type"]
	image = ["https://drop.ndtv.com/albums/COOKS/chicken-dinner/chickendinner_640x480.jpg","http://www.executivefranchises.com/wp-content/uploads/2013/10/Food-Franchise-Opportunities-today.jpg","http://ugo.co.ug/wp-content/uploads/2017/11/fast-food.jpg"]
	diet = ["Classic","Vegetarian","Vegan","Diabetic"]
	recipes = recipe_names.split("\n")
	for x in range(len(recipes)):
		preptime = str(randint(10, 250))
		cooktime = str(randint(10, 250))
		image = image[(randint(1,3))]
		serving = str(randint(1,5))
		recipe = add_quotes(recipes[x].strip())
		vals = [recipe,image, preptime,cooktime,serving, add_quotes(fake.date()),diet]
		f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
	for x in range(NUM_RECIPES-len(recipes)):
		fake.seed(x)
		preptime = str(randint(10, 250))
		cooktime = str(randint(10, 250))
		image = image[(randint(1,3))]
		serving = str(randint(1,5))
		recipe = add_quotes(fake.word())
		vals = [recipe,image, preptime,cooktime,serving, add_quotes(fake.date()),diet]
		f.write(BASE_INSERT.format(table, ",".join(fields), ", ".join(vals))+"\n")
	f.close()

def generate_instr():
	verbs = ['Add', 'adjust', 'arrange', 'bake', 'baste', 'batter', 'beat', 'blend', 'boil', 'braise', 'break', 'broil', 'brush', 'burn', 'carve', 'chill', 'chop', 'clarify', 'crack', 'cook', 'cool', 'cover', 'cut', 'Debone', 'dice', 'discard', 'drain', 'dress', 'fillet', 'flour', 'fold', 'freeze', 'fry', 'garnish', 'glaze', 'grate', 'grind', 'grill', 'gut', 'heat', 'knead', 'Lower', 'macerate', 'marinate', 'mash', 'melt', 'mince', 'mix', 'parboil', 'peel', 'pickle', 'place', 'poach', 'pour', 'prepare', 'put', 'reduce', 'refrigerate', 'remove', 'rinse', 'roast', 'roll out', 'roll up', 'rub', 'Salt', 'saut\xc3\xa9', 'scoop', 'scorch', 'scramble', 'season', 'serve', 'set', 'simmer', 'skim', 'slice', 'soak', 'spice', 'spoon', 'spread', 'sprinkle', 'squeeze', 'steam', 'stir', 'strain', 'sugar', 'sweeten', 'taste', 'thaw', 'thicken', 'toast', 'try', 'warm', 'wash', 'water down', 'whip', 'whisk', 'wipe']

	ingredients = ingredient_list.split("\n")
	table = "instruction"
	fields = ["recipe_id", "instruction_id","step_num","direction"]
	instruction_format = "{} the {} ."
	f = open("db_data.sql", "w")
	for verb in verbs:
		for ingredient in ingredients:
			for x in range(1, NUM_RECIPES - 1):
				insts = randint(2,9)
				used = set([])
				for y in range(insts):
					while True:
						inst = randint(1, 12610)
						if inst in used:
							continue
						else:
							vals = [str(x), str(inst), str(y+1),add_quotes(instruction_format.format(verb, ingredient))]
							f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
							

	f.close()

def generate_recipe_instr():
	f = open("db_data.sql", "a+")
	table = "follow_instruction"
	fields = ["recipe_id", "instruction_id","instruction_order"]
	for x in range(1, NUM_RECIPES - 1):
		insts = randint(2,9)
		used = set([])
		for y in range(insts):
			while True:
				inst = randint(1, 12610)
				if inst in used:
					continue
				else:
					vals = [str(x), str(inst), str(y+1)]
					used.add(inst)
					f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
					break

	f.close()

def generate_ingr_rec():
	f = open("db_data.sql", "w")
	table = "needs"
	fields = ["ingredient_id", "recipe_id","measurement_id", "quantity"]
	for x in range(1, NUM_RECIPES + 1):
		ingrs = randint(1,7)
		used = set([])

		for y in range(ingrs):
			meas = randint(1,9)
			quantity = randint(1,10)
			while True:
				ingr = randint(1, 130)
				if ingr in used:
					continue
				else:
					vals = [str(ingr), str(x), str(meas), str(quantity)]
					used.add(ingr)
					f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
					break
	f.close()

MEALPLANS= 10
MEALPLANDAYS=35

def generate_meal():
	recipes = recipe_names.split("\n")
	f = open("db_data.sql","a+")
	table = "meal"
	fields = ["meal_name","mealtype","num_calorie","day"]
	types = ["Breakfast", "Lunch", "Dinner"]
	days =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
	for x in range(0,MEALPLANDAYS-1):
		name = add_quotes(recipes[x].strip())
		mealtype = add_quotes(types[randint(0,2)])
		mealdays = add_quotes(days[randint(0,6)])
		calories = str(randint(250, 2000))
		vals = [name,mealtype,calories,mealdays]
		f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals))+"\n")
	f.close()



def generate_mealplan():
	f = open("db_data.sql","a+")
	table = "mealplan"
	f.close()


def generate_planmeal():
	f = open("db_data.sql","a+")
	table = "plan_generate"
	fields =["mealplan_id","meal_id"]
	for x in range(0,MEALPLANS-1):
		mealplandays = randint(1,MEALPLANDAYS)
		for y in range(mealplandays):
			vals = [str(x),str(mealplandays)]
			f.write(BASE_INSERT.format(table, ", ".join(fields), ", ".join(vals)) + "\n")
			break
	f.close()

generate_user(NUM_USERS)
generate_recipe()
generate_ingr()
generate_instr()
generate_ingr_rec()
generate_recipe_instr()
