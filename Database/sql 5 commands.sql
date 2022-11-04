select * from Computer;

-- cross join as Cartesian Product

select 
S.StudentId, S.Fname as FirstName, S.StudentId, C.StudentId as Comp_alloc_stud, C.Model
from Student S 
cross join Computer C;  

-- Inner join

select

Fname as Firstname, S.StudentId as Stu_StudentId, C.StudentId as Com_StudentId, Model
from Student S inner join Computers C on S.StudentId = C.StudentId;

create table Employee(
	id integer primary key,
    ename varchar(20),
    dept varchar(10),
    compid integer
);

select * from Employee;

select * from Computer;

drop table Computer;

truncate table Computer;

insert into Employee values(1, "Vinay", "ICP", 1001);
insert into Employee values(2, "Kumar", "ETA", NULL);
insert into Employee values(3, "Raju", "ETA", 1002);
insert into Employee values(4, "Manoj", "ETA", NULL);
insert into Employee values(5, "Sai", "ICP", 1003);

alter table Employee add manager integer;

update Employee set manager = null where id = 1;
update Employee set manager = null where id = 2;
update Employee set manager = 2 where id = 3;
update Employee set manager = 2 where id = 4;
update Employee set manager = 1 where id = 5;

create table Computer(
	compid integer primary key,
    make varchar(20),
    model varchar(20),
    myear varchar(10)
);

insert into Computer values(1001, "DELL", "Vostro", 2013);
insert into Computer values(1002, "DELL", "Precision", 2014);
insert into Computer values(1003, "LENOVO", "Edge", 2013);
insert into Computer values(1004, "LENOVO", "Horizon", 2014);

select 
id, ename, e.compid as e_compid, c.compid as c_compid, model 
from Employee e inner join Computer c 
on e.compid = c.compid;

select 
id, ename, e.compid as e_compid, c.compid as c_compid, model 
from Employee e inner join Computer c 
on e.compid = c.compid
where dept = "ETA";

select 
id, ename, e.compid as e_compid, c.compid as c_compid, model 
from Employee e inner join Computer c 
on e.compid = c.compid
and dept = "ETA";

-- Self join 
 
select 
e.id as empid, e.ename as empname, m.id as mgrid, m.ename as mgrname 
from Employee e inner join Employee m 
on e.manager = m.id;

-- Outer join 
-- Left Outer join

select 
id, ename, e.compid as e_compid, c.compid as c_compid, model 
from Employee e left outer join Computer c 
on e.compid = c.compid;

select 
id, ename, e.compid as e_compid, c.compid as c_compid, model 
from Employee e left outer join Computer c 
on e.compid = c.compid
where dept="ETA";

-- Right Outer join

select 
id, ename, e.compid as e_compid, c.compid as c_compid, model 
from Employee e right outer join Computer c 
on e.compid = c.compid;
 
select 
id, ename, e.compid as e_compid, c.compid as c_compid, model 
from Employee e right outer join Computer c 
on e.compid = c.compid
where dept = "ETA";

-- from,  join, where, select 

-- full outer join 
select 
id, ename, e.compid as e_compid, c.compid as c_compid, model 
from Employee e left outer join Computer c 
on e.compid = c.compid
union
select 
id, ename, e.compid as e_compid, c.compid as c_compid, model 
from Employee e right outer join Computer c 
on e.compid = c.compid;











