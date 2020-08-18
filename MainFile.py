import os
import Database
import StudentClass

while(True):
    print("1. Insert Student Detail.\n2. Update Student Detail.\n3. Delete Student Detail.\n4. Display Student Detail.\n5. Exit.")
    
    try:
        ch=int(input("Enter your choice :"))
        if(ch==1):
            StudentObj=StudentClass.Student()
        elif(ch==2):
            Enrollment=input("Enter Enrollment Number :")
            StudentClass.Student.DisplayStudentDetails(Enrollment)
            StudentClass.Student.UpdateStudentDetails(Enrollment)

        elif(ch==3):
            Enrollment=input("Enter Enrollment Number :")
            StudentClass.Student.DeleteStudentDetails(Enrollment)
        elif(ch==4):

            
            Enrollment=input("Enter Enrollment Number :")
            StudentClass.Student.DisplayStudentDetails(Enrollment)
        elif(ch==5):
            break
        else:
            print("Please Enter Valid Input!....")
        
    except Exception as e:
        print(str(e))
    finally:
        Database.Connection.commit()
        input("Press Any Key To Continue...")
        os.system('cls')
       
        