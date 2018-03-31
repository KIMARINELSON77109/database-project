drop database if EXISTS ultimate_meal_planner;
create database ultimate_meal_planner;
use ultimate_meal_planner;

drop table if exists user;
create table user
(
	user_id     int not null UNIQUE auto_increment,
	firstname   varchar(255) not null,
	lastname    varchar(255) not null,
	D_O_B       varchar(255) not null,
	email		varchar(255) not null UNIQUE,
	phone       varchar(255) not null,
	password    varchar(255) not null,
	primary key (user_id)
) ENGINE=INNODB;

drop table if exists recipe;
create table recipe
(
	recipe_id	     int not null auto_increment,
	recipe_name	     varchar(120) not null,
	recipe_picture   varchar(99) not null,
	prep_time	     varchar(12) not null,
	cook_time        varchar(10) not null,
	servings         int not null,
	diet_type        varchar(10) not null,
	primary key(recipe_id)
) ENGINE=INNODB;

drop table if exists measurement;
create table measurement
(
	measurement_id      int not null auto_increment,
	measurement_name    varchar(15) not null,
	primary key(measurement_id)
) ENGINE=INNODB;

drop table if exists ingredients;
create table ingredients
(
	ingredient_id		int not null auto_increment,
	ingredient_name	    varchar(15) not null,
	primary key(ingredient_id)
) ENGINE=INNODB;

drop table if exists add_recipe;
create table add_recipe
(
	user_id       int not null,
	recipe_id     int not null,
	date_created  date not null,
	primary key(recipe_id,user_id),
	FOREIGN key(user_id) REFERENCES user(user_id) on delete RESTRICT,
	FOREIGN key(recipe_id) REFERENCES recipe(recipe_id) on  delete RESTRICT
)ENGINE=INNODB;

drop table if exists instruction;
create table instruction
	(
		instruction_id  int not null auto_increment,
		recipe_id       int not null,
		step_num        int not null,
		direction       varchar(100),
		primary key (instruction_id,recipe_id),
		foreign key (recipe_id) references recipe(recipe_id) ON DELETE RESTRICT
	)ENGINE=INNODB;
	
drop table if exists meal_type;
create table meal_type
(
	meal_type_id	  int not null auto_increment,
	meal_type		  varchar(10) UNIQUE not null,
	primary key(meal_type_id)
) ENGINE=INNODB;

drop table if exists diet;
create table diet
(
	diet_type_id	  int not null auto_increment,
	diet_type		  varchar(10) UNIQUE not null,
	primary key(diet_type_id)
) ENGINE=INNODB;


drop table if exists meal_plan;
create table meal_plan
(
	mealplan_id		  int not null UNIQUE auto_increment,
	end_date          date not null,
	PRIMARY key(mealplan_id)
) ENGINE=INNODB;

drop table if exists plan_generate;
CREATE TABLE plan_generate
(
	user_id       INT NOT NULL,
	mealplan_id   INT NOT NULL,
	PRIMARY KEY(user_id, mealplan_id),
	FOREIGN KEY(user_id) references user(user_id) on delete restrict,
	FOREIGN KEY(mealplan_id) references meal_plan(mealplan_id) on delete restrict
)ENGINE=INNODB;

drop table if exists meal;
create table meal
(
 	meal_id			  int not null auto_increment,
 	meal_name		  varchar(15) not null,
 	meal_type		  varchar(10) not null,
	num_calorie       int not null,
	day               varchar(10) not null,
 	primary key(meal_id)
) ENGINE=INNODB;

drop table if EXISTS profile;
create table profile
(
	profile_id		int not null auto_increment,
	user_id         Int not null,
	diet_type       varchar(10) not null,
	primary key(profile_id),
	FOREIGN key(user_id) REFERENCES user(user_id) on delete RESTRICT
) ENGINE=INNODB;


drop table if exists makes;
create table makes
(
	meal_id    int not null,
	recipe_id  int not null,
	primary key (recipe_id,meal_id),
	FOREIGN key (meal_id) REFERENCES meal(meal_id) on update cascade on delete cascade,
	FOREIGN key (recipe_id) REFERENCES recipe(recipe_id) on update cascade on delete restrict
)ENGINE=INNODB;

drop table if exists needs;
create table needs
(
	ingredient_id         int not null,
	recipe_id             int not null,
	quantity			  FLOAT not null,
	measurement_id		  int not null,
	primary key (ingredient_id,recipe_id),
	FOREIGN key (ingredient_id) REFERENCES ingredient(ingredient_id) on delete restrict,
	FOREIGN key (recipe_id) REFERENCES recipe(recipe_id) on delete restrict,
	foreign key(measurement_id) references measurement(measurement_id) ON DELETE RESTRICT
)ENGINE=INNODB;

drop table if exists contains;
create table contains
(
	mealplan_id 	int not null,
	meal_id         int not null,
	primary key(meal_id,mealplan_id),
	FOREIGN key(mealplan_id) REFERENCES meal_plan(mealplan_id) on DELETE RESTRICT,
	FOREIGN key(meal_id) REFERENCES meal(meal_id) on DELETE RESTRICT
)ENGINE=INNODB;
