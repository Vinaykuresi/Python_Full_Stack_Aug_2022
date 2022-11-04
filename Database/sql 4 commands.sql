
use School;
-- selects all records from tabl3e-- 
select
*
from Student;

-- order by
select 
StudentId, Fname as FullName 
from Student 
order by studentId asc; 

select 
StudentId, Fname as FullName 
from Student 
order by 2; 

select
*
from Student
where StudentId < 1004
order by Fname asc;


select 
StudentId, Fname as FullName 
from Student 
order by studentId desc; 

select 
StudentId, Fname as FullName 
from Student 
order by Fname asc, studentId desc;

select 
*
from Student;

-- Distinct 
select 
distinct Address 
from Student; 

select 
StudentId, Fname as FullName 
from Student;

-- group by
select 
Address, count(StudentId) as TotalStudents
from Student
group by Address;

select 
Dept, sum(price)
from Student
group by Dept;

select 
Dept, count(StudentId) as total_no_students
from Student
group by Dept;

select 
Dept, Branch, Max(Price) 
from Student
group by Dept, Branch;

select 
Dept, max(Price), min(Price)
from Student 
group by Dept;

select 
Dept, Branch, Max(Price) 
from Student
group by Dept;

select
count(StudentId) as Count 
from Student;

select 
Dept, count(StudentId) as Count
from Student
group by Dept; 

select
Dept, Branch, max(Price) as Max_Fees 
from Student 
group by Dept, Branch;

-- Having Clause 
select 
Dept, avg(Price) as Average_Fees
from Student 
group by Dept 
having avg(Price) > 38500;

-- 1) From 2) group 3) having 4) select

-- price > 35000
-- studentId > 1

select 
Dept, sum(Price) as Total_Fees 
from Student 
where Price > 35000
group by Dept 
having count(StudentId) > 1;

select 
Dept, sum(Price) 
from Student 
where Price >= 30000
group by Dept
having count(StudentId) > 1;

select
distinct Dept
from Student
where Price > 30000 
order by Dept;

-- computer table

CREATE TABLE Computers(
	Make varchar(20),
    StudentId integer,
	foreign key (StudentId) REFERENCES Student(StudentId) ,
    Model varchar(20),
    MYear integer
); 

INSERT INTO Computers values("Dell", 1001, "Vostro", 2020);
INSERT INTO Computers values("Lenevo", 1002, "Edge", 2019);
INSERT INTO Computers values("Dell", 1003, "Precision", 2018);
INSERT INTO Computers values("Lenevo", 1004, "Horizon", 2019);
INSERT INTO Computers values("Asus", 1005, "Vivobook", 2018);
INSERT INTO Computers values("Asus", 1006, "Zenbook", 2020);

select
*
from Computers; 

-- Cross Join

select 
Stu.StudentId, Stu.Fname as Firstname, Com.StudentId, Com.Make 
from Student Stu cross join Computers Com; 


-- Inner Join
select
Stu.StudentId, Stu.Fname as FirstName, Stu.Dept, Com.Make, Com.Model 
from Student Stu inner join Computers Com 
on Stu.StudentId = Com.StudentId;






 
