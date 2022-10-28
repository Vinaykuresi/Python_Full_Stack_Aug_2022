-- Numeric Functions
select * from Student;

alter table Student Add Price integer;

update Student set Price = 35000 where StudentId = 1004;
update Student set Price = 25000 where StudentId = 1005;
update Student set Price = 50000 where StudentId = 1006;

-- absolute function
select abs(-12);

-- avg function
select avg(Price) as AverageFees from Student;

-- count function
select count(StudentId) As NumberOfStudents from Student; 

-- sum function
select sum(Price) as TotalPrice from Student;

-- max function
select max(Price) as TotalPrice from Student;

-- min function
select min(Price) as TotalPrice from Student;

select max(Price) as MaxPrice,  min(Price) as MinPrice from Student;

-- Character Function

-- Concat function
select concat("Vinay ", " Kumar ", " Kuresi") as FullName;  

-- insert function
select insert("Garuda Careers", 1, 6, "KVK"); 

-- Lower case
select LCASE("GARUDA CAREERS"); 

-- replace function
select replace("Garuda Careers", "Garuda", "KVK"); 

-- position
select position("u" in "Garuda Careers") as MatchPosition;

-- reverse function
select reverse("1ABCBA2");

-- Date function

-- addDate function
select adddate("2022-10-28", interval 5 day); 

-- addTime 
select addtime("2022-10-28 06:41:30", "30");

-- curDate
select curdate(); 

-- current time
select current_time(); 

-- current timestamp 
select current_timestamp();

-- date
select date("2022-10-28 06:41:30"); 

-- Conversion function

-- convert function
select convert("2022-10-28", date);

select convert(200, char);

select convert(3-5, unsigned);


