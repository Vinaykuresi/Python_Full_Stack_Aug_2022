-- all columns 
select * from Student;

-- specific columns
select StudentId, Fname from Student; 

-- As ~ Alias
 select StudentId, Fname as FirstName from Student; 
 
 -- new student IDs
 select StudentId * 2 as New_Student_Ids from Student;
 
 -- Distinct
 select distinct Address from Student;
 
  -- deleting the record
 delete from Student where StudentId = 1006;
 
 select distinct Fname as Firstname, Address from Student;
 
 -- Where NULL
 select Fname as FirstName, StudentId from Student where StudentId > 1003;
 
 select Fname as FirstName, StudentId from Student where Fname = "Suresh";
 
 -- And Operator
  select 
  Fname as FirstName, StudentId 
  from Student 
  where StudentId > 1002 and StudentId < 1005;
  
  -- OR Operator
  select 
  Fname as FirstName, StudentId 
  from Student 
  where StudentId > 1002 OR StudentId < 1005;
 
-- Between Operator
  select 
  Fname as FirstName, StudentId 
  from Student 
  where StudentId between 1002 and 1005;
 
 -- IN Operator
  select 
  *
  from Student 
  where StudentId IN (1002, 1003, 1005);
  
  -- NOT Operator
  select 
  *
  from Student 
  where StudentId NOT IN (1002, 1003, 1005);
  
-- all columns 
select 
* 
from Student;
  
-- Insert data into Specific columns 
INSERT 
INTO Student(StudentId, Address) 
values(1006, "Tirupati, AP");
 
 -- Filter on NULL
 select 
 StudentId, Address
 from Student
 where Fname = null;
 
 -- IS NULL
 select 
 StudentId, Address
 from Student
 where Fname is null;
 
 -- character selection
 select
 *
 from Student
 where DOJ like "1994%";
 
 
 