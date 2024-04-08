
import numpy as np
import ManagerClass
import System
import Student
import Subject


print("\n-------------------------\n     Ajou University     \n-------------------------") 

while(1): 
    print("\nChoose the option you want.")
    print("1. Join membership")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter the number : ")
    match choice: # 회원가입 반복문
        case '1':
            System.membership()
        case '2': #Login 아이디중복X
            ID, Password = System.login()
            if ID == '': continue # 사용자가 
            Subject.get()
            if System.getType(ID) == "Manager" :
                User = ManagerClass.Manager()
                # while 1:
                #     if Manager.Choice() == 4 : break
                #     else : continue  
            else : User = StudentChoice.Student(ID) # UserList[ID][Password] == "Student"

            User.Choice()

        case '3': #Exit
             exit()
             
        case _: #Wrong Choice
             print("\n1-This option is not available. Please enter the available number.")
             continue
