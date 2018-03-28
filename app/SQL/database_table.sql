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
	recipe_name	     varchar(15) not null,
	recipe_picture   varchar(99) not null,
	prep_time	     varchar(12) not null,
	cook_time        varchar(10) not null,
	servings         int not null,
	primary key(recipe_id)
) ENGINE=INNODB;