create schema if not exists company_constraints;
use company_constraints;

select * from information_schema.table_constraints
	where constraint_schema = 'company_constraints';

-- restrição atribuída a um domínio
-- create domain D_num as int check(D_num > 0 and D_num < 21);

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
    constraint chk_salary_employee check (Salary > 2000.0),
    constraint pk_employee primary key (Ssn)
);

desc employee;

create table department(
	Dname varchar(15) not null,
    Dnumber int not null,
    Mgr_ssn char(9) not null,
    Mgr_start_date date,
    Dept_create_date date,
    constraint chk_date_dept check (Dept_create_date < Mgr_start_date),
    constraint pk_dept primary key (Dnumber),
    constraint unique_name_dept unique (Dname),
    foreign key (Mgr_ssn) references employee(Ssn)
);

desc department;

create table dept_locations(
	Dnumber int not null,
    Dlocation varchar(15) not null,
    constraint pk_dept_locations primary key (Dnumber, Dlocation),
    constraint fk_dept_locations foreign key (Dnumber) references department(Dnumber)
);

create table project(
	Pname varchar(15) not null,
    Pnumber int not null,
    Plocation varchar(15),
    Dnum int not null,
    primary key (Pnumber),
    constraint unique_project unique (Pname),
    constraint fk_project foreign key (Dnum) references department(Dnumber)
);

create table works_on(
	Essn char(9) not null,
    Pno int not null,
    Hours decimal(3,1) not null,
    primary key (Essn, Pno),
    constraint fk_employee_works_on foreign key (Essn) references employee(Ssn),
    constraint fk_project_works_on foreign key (Pno) references project(Pnumber)
);

create table dependent(
	Essn char(9) not null,
    Department_name varchar(15) not null,
    Gender char, -- F or M,
    Bdate date,
    Relationship varchar(8),
    Age int not null,
    constraint chk_age_dependednt check (Age < 22),
    primary key (Essn, Department_name),
    constraint fk_dependent foreign key (Essn) references employee(Ssn)
);

show tables;
desc dependent;
    
select * from information_schema.referential_constraints
	where constraint_schema = 'company_constraints';