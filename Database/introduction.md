
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