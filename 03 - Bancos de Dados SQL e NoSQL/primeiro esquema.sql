show databases;
create database if not exists first_example;
use first_example;
create table person(
person_id smallint unsigned,
fname varchar(20),
lname varchar(20),
gender enum('M', 'F'),
birth_date DATE,
street varchar(20),
city varchar(20),
state varchar(20),
country varchar(20),
postal_code varchar(20),
constraint pk_person primary key (person_id)
);
show tables;
desc person;

create table favorite_food(
person_id smallint unsigned,
food varchar(20),
constraint pk_favorite_food primary key (person_id, food),
constraint fk_favorite_food_person_id foreign key (person_id) references person(person_id)
);
desc favorite_food;
select * from information_schema.table_constraints
where constraint_schema = 'first_example';
select * from information_schema.table_constraints
where table_name = 'person';
select * from information_schema.table_constraints
where constraint_schema = 'first_example';

insert into person values ('1', 'Henrique', 'Klein', 'M', '1985-11-11', 'Rua Cristóvão', 'Cidade C', 'RS', 'Brasil', '55555-05');
select * from person;
insert into person values ('2', 'Igor', 'Guimarães', 'M', '1999-12-01', 'Rua Tenório', 'Cidade B', 'SP', 'Brasil', '88888-05'),
('3', 'Juliana', 'Serqueira', 'F', '1989-05-07', 'Rua Pixirico', 'Cidade A', 'RJ', 'Brasil', '99999-05');
insert into person values ('4', 'Igor', 'Guimarães', 'M', '1999-12-01', 'Rua Tenório', 'Cidade B', 'SP', 'Brasil', '88888-05'),
('5', 'Juliana', 'Serqueira', 'F', '1989-05-07', 'Rua Pixirico', 'Cidade A', 'RJ', 'Brasil', '99999-05');
delete from person where person_id=4 or person_id=3;

insert into favorite_food values (1, 'lasanha'), (2, 'churrasco'), (5, 'macarrão');
select * from favorite_food;