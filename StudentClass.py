import Database
import Validation
class Student:

    #Init Method to initialize Student Object and Insert Data Into DataBase...
    def __init__(self):
       
        self.FirstName=input("Enter First Name :")
        self.LastName=input("Enter Last Name :")

        #Validation To Check Enrollment Number Is Valid Or Not...
        while(True):
            self.EnrollmentNumber=input("Enter Enrollment Number :")
            if(not Validation.DataValidationEnroll(self.EnrollmentNumber)):
                print("<<<<     Please Enter Valid Enrollment Number!...     >>>>")
                continue
            break
        
        #Validation To Check Email Is Valid Or Not...
        while(True):
            self.Email=input("Enter Email :")
            if(not Validation.DataValidationEmail(self.Email)):
                print("<<<<     Please Enter Valid Email!...     >>>>")
                continue
            break

        self.City=input("Enter City Name:")
        Database.Curcer.execute("Insert into StudentDetail (FirstName,LastName,EnrollmentNumber,Email,City) Values(?,?,?,?,?)",(self.FirstName,self.LastName,self.EnrollmentNumber,self.Email,self.City))
        Database.Connection.commit()
        print("Your Data Inserted Successfully")



    @staticmethod    
    def DisplayStudentDetails(Enrollment):
        Database.Curcer.execute("SELECT * FROM StudentDetail WHERE EnrollmentNumber=?",(Enrollment,))
        lst=Database.Curcer.fetchall()
        if(len(lst)==0):
            print("<<<<     Record is not exists!...     >>>>")
        else:
            Student=lst[0]
            print("==========================================")
            print("First Name :",Student[0])
            print("Last Name :",Student[1])
            print("Enrollment Number :",Student[2])
            print("Email :",Student[3])
            print("City :",Student[4])
            print("==========================================")

    @staticmethod
    def DeleteStudentDetails(Enrollment):
        Database.Curcer.execute("DELETE FROM StudentDetail WHERE EnrollmentNumber=?",(Enrollment,))
        deleted_rows=Database.Curcer.rowcount
        if(deleted_rows==1):
            Database.Connection.commit()
            print("Record Deleted Succesfully.")
        else:
            print("Record Not Found...")
    @staticmethod
    def UpdateStudentDetails(Enrollment):
        print("Enter Details where you have to Update it.")
        FirstName=input("Enter First Name :")
        LastName=input("Enter Last Name :")

        #Validation To Check Email Is Valid Or Not...
        while(True):
            Email=input("Enter Email :")
            if(not Validation.DataValidationEmail(Email)):
                print("<<<<     Please Enter Valid Email!...     >>>>")
                continue
            break

        City=input("Enter City Name:") 
        Database.Curcer.execute("update StudentDetail set FirstName=?,LastName=?,Email=?,City=? where EnrollmentNumber=?",(FirstName,LastName,Email,City,Enrollment))
        Database.Connection.commit()
        print("Your Data Updated Successfully")

    
