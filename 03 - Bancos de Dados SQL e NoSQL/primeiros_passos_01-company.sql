create schema if not exists company;
use company;

create table employee(
	Fname varchar(15) not null,
	Minit char,
	Lname varchar(15) not null,
	Ssn char(9) not null, -- char specifies that it must contain exactly 9 characters
	Bdate date,
	Address varchar(30),
	Gender char,
	Salary decimal(10,2),
	Super_ssn char(9),
	Dno int not null,
    primary key (Ssn)
);

create table department(
	Dname varchar(15) not null,
    Dnumber int not null,
    Mgr_ssn char(9) not null,
    Mgr_start_date date,
    Dept_create_date date,
    primary key (Dnumber),
    Unique (Dname),
    foreign key (Mgr_ssn) references employee(Ssn)
);

create table dept_locations(
	Dnumber int not null,
    Dlocation varchar(15) not null,
    primary key (Dnumber, Dlocation),
    foreign key (Dnumber) references department(Dnumber)
);

create table project(
	Pname varchar(15) not null,
    Pnumber int not null,
    Plocation varchar(15),
    Dnum int not null,
    primary key (Pnumber),
    unique (Pname),
    foreign key (Dnum) references department(Dnumber)
);

create table works_on(
	Essn char(9) not null,
    Pno int not null,
    Hours decimal(3,1) not null,
    primary key (Essn, Pno),
    foreign key (Essn) references employee(Ssn),
    foreign key (Pno) references project(Pnumber)
);

create table dependent(
	Essn char(9) not null,
    Department_name varchar(15) not null,
    Gender char, -- F or M,
    Bdate date,
    Relationship varchar(8),
    primary key (Essn, Department_name),
    foreign key (Essn) references employee(Ssn)
);

show tables;
desc dependent;