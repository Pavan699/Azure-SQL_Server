'''
@Author: Pavan Nakate
@Date: 2022-01-11 8:30
@Last Modified by: Pavan Nakate
@Last Modified time: 2022-01-11
@Title : SQL-Server-Connection
'''
import pymssql
import json

class SQL_Server_Connection:
    """
    Description:
        Class for all the methods to manipulate the SQL database in Aure
    """
    
    def __init__(self,servername,username,password,dbname) -> None:
            """
            Description:
                Function for a connection and cursor object as a property of class
            Parameter:
                server name, username, password, databasename for connection
            Return:
                None
            """
            self.connection = pymssql.connect(server=servername, user=username, password=password, database=dbname)
            self.cursor = self.connection.cursor()

    def show(self):
            """
            Description:
                Function visualizes the table in database
            Parameter:
                self object is sufficient
            Return:
                None
            """
            self.cursor.execute('select * from student;')
            data = self.cursor.fetchall()
            for i in data:
                print(i)

    def data():
            """
            Description:
                Function is to enter new data which is call by add data method
            Parameter:
                no parameter
            Return:
                all the entities in dictionary format
            """
            stdid = input('Enter Emp ID : ')
            Fname = input('Enter First Name : ')
            Lname = input('Enter Last Name : ')
            dep = input('Enter Department : ')
            contact = input('Enter contact number : ')
            return {
                'stdid': stdid,
                'Fname': Fname,
                'Lname': Lname,
                'dep': dep,
                'contact': contact
            }

    def add(self):
            """
            Description:
                Function is to enter new data into table
            Parameter:
                self object is sufficenrt
            Return:
                None
            """
            dict = SQL_Server_Connection.data()
            self.cursor.execute(
                f"insert into student values ({dict['stdid']},'{dict['Fname']}','{dict['Lname']}',{dict['sal']},'{dict['dep']}',{dict['contact']})"
            )
            self.connection.commit()

    def update(self):
            """
            Description:
                Function is to update entities in table
            Parameter:
                self object is sufficenrt
            Return:
                None
            """
            userInput = input('Enter Student ID to Edit specific student data : ')
            dict = SQL_Server_Connection.data()
            self.cursor.execute(
                f"UPDATE student SET Std_id={dict['stdid']},First_name='{dict['Fname']}',Last_name='{dict['Lname']}',`salary`={dict['sal']},`department`='{dict['dep']}',contact_Number={dict['contact']} WHERE emp_id='{userInput}'"
            )
            self.connection.commit()

    def delete(self):
            """
            Description:
                Function is to delete entity from table
            Parameter:
                self object is sufficenrt
            Return:
                None
            """
            userInput = input('Enter Student ID to delete specific student data : ')
            self.cursor.execute(
                f"DELETE FROM student WHERE Std_id='{userInput}'")
            self.connection.commit()

    def DummyData(self):
            """
            Description:
                Function is to enter dummy data into table
            Parameter:
                self object is sufficenrt
            Return:
                None
            """
            self.cursor.execute(
                f"insert into student values (01,'Pavan','Nakate','Civil',9960748875),(02,'Abhi','Shinde','ENTC',8855223366),(03,'Simran','Shaikh','BSC',9876543210),(04,'Ajinky','Mane','ENTC',8855223366),(05,'Afrin','Mulla','Mech',9876543210);")
            self.connection.commit()
    
    def DummyData2(self):
            """
            Description:
                Function is to enter dummy data into table
            Parameter:
                self object is sufficenrt
            Return:
                None
            """
            self.cursor.execute(
                f"insert into student values (01,'Pavan','Nakate','Civil',9960748875),(02,'Abhi','Shinde','ENTC',8855223366),(03,'Simran','Shaikh','BSC',9876543210);")
            self.connection.commit()

    def DeleteAllData(self):
            """
            Description:
                Function is to delete all entities from table
            Parameter:
                self object is sufficenrt
            Return:
                None
            """
            self.cursor.execute("truncate table student;")
            self.connection.commit()

    def CreateTable(self,query=""):
            """
            Description:
                Function is to create a new table
            Parameter:
                self object is sufficenrt
            Return:
                None
            """
            default_query="CREATE TABLE student(Std_id int,First_name varchar(50),Last_name varchar(50),department varchar(50),contact_number bigint)"
            if query=="":
                query=default_query
            self.cursor.execute(query)
            self.connection.commit()


if __name__ == "__main__":

    
    #opening json file having all the creadential data of azure storage accout
    with open('data.json','r') as jf:
        data1 = json.load(jf)

    server_name = data1['server_name']
    user_name_SQL = data1['user_name_SQL']
    password_SQL = data1['user_password_SQL']
    database_name = data1['user_database_name']
    

    sqldata = SQL_Server_Connection(server_name,user_name_SQL,password_SQL,database_name)
    sqldata.CreateTable()
    #sqldata.add()
    #sqldata.update()
    #sqldata.DummyData()
    #sqldata.show()
    #sqldata.DummyData2()
    #sqldata.delete()
    #sqldata.DeleteAllData()