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

select StudentId,  Fname as FirstName from Student where StudentId <= 1004;

alter table Student drop column DOJ;

alter table Student Add Address varchar(20);

alter table Student modify column Fname varchar(20);

INSERT INTO Student(StudentId, Address) values(1006, "Tirupati, AP");

update Student set Address = "Hyderabad, Telangana" where StudentId = 1004;

delete from Student where StudentId = 1005;

truncate table Student;

select distinct Address from Student;

select StudentId, Fname from Student where StudentId > 1002 and StudentId < 1005;

select StudentId, Fname from Student where StudentId > 1002 or StudentId < 1005;

select StudentId, Fname from Student where StudentId in (1001, 1003, 1005);

select StudentId, Fname from Student where StudentId not in (1001, 1003, 1005);

select StudentId, Fname from Student where Gender is not Null;

select * from Student where Fname like "S%";
select * from Student where Fname like "%es%";

select * from Student where DOJ like '%04%';

select * from Student where Fname like '_a%';

select * from Student where DOJ = '1992-11-05' or DOJ = '1993-03-23';

select min(StudentId) as FirstStudentId, max(StudentId) as LastStudentId from Student;











