
DBMS(Database management system) : 
1) Data structure (format) -> in the way a data will be stored.
    ex : XML, Windows.registry

    logic : [{
        cust_id : 1001,
        name : "Vinay",
        address : "Tiruapti"
    },
    {
        cust_id : 1001,
        name : "Vinay",
        address : "Tiruapti"
    },
    {
        cust_id : 1001,
        name : "Vinay",
        address : "Tiruapti"

    }] -> 1) nosql database

          2) heirarical database

          3) Network database 

          4) rdbms database 

RDBMS(Relational Database management system) : 
    ex : 

    1) Customer : 
        1) Primary key
        2) Numerical type -> data type or check constraint
        Customer ID     Customer Name       Contact name        address
        1001            Vinay               vinay               tirupati
        2002            Kumar               rajesh              hyderabad
        3003            suresh              suresh              bangalore
        4004            praveen             lilly               tirupati

    2) Orders : 
                        3) Foriegn key
        Order ID        Customer ID         Employee ID         Order Date
        10301           4004                A204                20-08-2022
        10302           4004                A204                22-08-2022
        10303           NULL                A202                19-08-2022
        10304           1001                A201                07-08-2022

        SQL -> structured query language

    3) Employee :
    Yes, Candidate key  NO              Yes             No           No
    Yes, Primary Key    NO              Yes             No           No
        Employee_No     Emp_Name        Aadhar_no       Salary       Date_of_birth 
        1001            Vinay           23745174        34000        17-04-1995
        2002            Kumar           23756127        23000        23-06-2000         
        3003            Suresh          23576277        45000        24-06-1998
        4004            Geetha          34756788        45000        18-06-2000

CREATE DATABASE SampleDB;

DDL Commnads : 
    1) Creation
    2) Modification
    3) Deletion.

        a) Tables
        b) Views
        c) Stored Proceedures
        4) indexs
        5) Constraints
    
    1) CREATE
    2) ALTER
    3) DROP
    4) TRUNCATE

DML Commands : 

    1) INSERT
    2) UPDATE
    3) DELETE
    4) SELECT

DCL Commands : 

    1) GRANT
    2) REVOKE

TCL Commands : 

    1) COMMIT
    2) ROLLBACK

SQL Chracter datatypes : 


                CHAR(n)                 VARCHAR(n)

Useful for      pre-determined          length vary a lot
                length

Storage size    n length                size of n characters
                characters                      +
                                        fixed size of store length

Example         CHAR(10) :              VARCHAR(10)
                "HELLO" -> 10 bytes     "Hello" -> 5 bytes + 2 bytes
            5 char + 5 trailing spaces  7 bytes
                10 bytes

Alternate Name  CHARACTER(N)            CHARACTER VARYING(N)

SQL Integral datatype :

    1) SMALLINT
    2) INTEGER
    3) BIGINT

SQL Non-Integral datatype : 

    1) Precision -> total no of digits | digts before + after : decimal points
    2) Scale -> no of digits after decimal point

    ex :  NUMERIC(3, 1) -> 23.1
          3 -> PRECISION
          1 -> SCALE

    Distinct :

        remove duplicates using Select clause


    Order of Query Execution : 

        FJWGHSDO -> 

            F -> From 
            J -> Join 
            W -> Where 
            G -> Group By 
            H -> Having 
            S -> Select 
            D -> Distinct 
            O -> Order By

    Function : 

        1) Numeric Function 
        2) Character Function 
        3) Conversion Function 
        4) Date Function 
        5) Aggregation Function 

                Aggregation fucntions operate on multiple rows to return a single row.

                ex : SUM(total), AVG(average)
                     MIN(lowest value), MAX(highest value), COUNT(number of rows) considers NULL, ex :  COUNT(*) 

Joins : 

    1) Inner Join :

            A and B -> A intersect B

    2) Self Join :

            A and A

    3) Left Outer Join :

            A and B -> Full A and comm B

    4) Right Outer Join :

            A and B -> Comm A and Full B

    5) Full Outer JOin :

            A and B -> Full A and Full B

    6) Cross Join( Cartesian Product Join ) :

            

    
