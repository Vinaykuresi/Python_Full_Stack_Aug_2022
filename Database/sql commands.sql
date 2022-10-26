CREATE DATABASE School;
show databases;

drop database School;

use school;

show tables;

CREATE table Student(
	StudentId	integer,
    Fname	varchar(10),
    Gender	char(1),
    DOJ		date
);

SHOW tables;

drop table Student;


CREATE table Student(
	StudentId  integer not null,
    Fname	varchar(10),
    Gender	char(1),
    DOJ		date
);

CREATE table Student(
	StudentId  integer,
    Fname	varchar(10),
    Gender	char(1),
    DOJ	date
);

select curdate();

CREATE table Student(
	StudentId  integer PRIMARY KEY,
    Fname	varchar(10),
    Gender	char(1),
    DOJ	date
);

CREATE table Student(
	StudentId  integer PRIMARY KEY,
    Fname	varchar(10),
    Gender	char(1) constraint Stud_gender_check check(Gender IN("M", "F")),
    DOJ	date
);

CREATE TABLE Marks(
	CourseId integer,
    StudentId integer,
	foreign key (StudentId) REFERENCES Student(StudentId) ,
    MarksScored decimal(5,2) 
);

drop table Marks;

CREATE TABLE Marks(
	CourseId integer,
    StudentId integer,
	foreign key (StudentId) REFERENCES Student(StudentId) ,
    MarksScored decimal(5,2),
    constraint marks_cid_pk primary key(CourseId, StudentId)
);

drop table Marks;

CREATE table Student(
	StudentId  integer PRIMARY KEY,
    Fname	varchar(10),
    Gender	char(1) constraint Stud_gender_check check(Gender IN("M", "F")),
    DOJ	date
);

INSERT INTO Student values(1001, "Vinay", "M", "1995-04-17");
INSERT INTO Student values(1002, "Varma", "F", "1994-04-14");
INSERT INTO Student values(1003, "Sukesh", "M", "1993-03-23");
INSERT INTO Student values(1004, "Suresh", "M", "1994-07-13");
INSERT INTO Student values(1005, "Gowtam", "M", "1992-11-05");

INSERT INTO Student values(1005, "Gowtam", "M", "1992-11-05");

select * from Student;

select StudentId, Fname from Student where StudentId <= 1004;

alter table Student drop column DOJ;

alter table Student Add Address varchar(20);

alter table Student modify column Fname varchar(20);

INSERT INTO Student(StudentId, Address) values(1006, "Tirupati, AP");

update Student set Address = "Warangal, Telangana" where StudentId = 1002;

delete from Student where StudentId = 1005;

truncate table Student;





