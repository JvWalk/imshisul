# import Manager
# import Student 
import numpy as np
# import managerCheck
import ManagerChoice
import Manager
import GwamokCaller
import GwamokShower


UserList = {} # 이중 dictionary형태 UserList = { ID : { Type : PW } }

# def managerCheck(CheckNum):
#     managerCheckNum = '1234'
#     if bool(CheckNum == managerCheckNum) : return CheckNum
#     else : return print("\nWrong Number.")

def getSubject():
    subjectFile = open("basics.txt", 'r')
    subject = subjectFile.readlines()
    subjectList = [x.split() for x in subject]
    subjectInfo = {}
    for i in subjectList: print(*i)
    # print(subjectInfo )
    # for i in subjectList:
    #     subjectInfo = {'과목번호':subjectList[i][0], '과목명':subjectList[i][1], '전필여부':subjectList[i][2], '학점':subjectList[i][3],'수업시간':subjectList[i][4], '장소':subjectList[i][5] }
    # print(subjectInfo)

# def addSubject():
       


print("\n-------------------------\n     Ajou University     \n-------------------------") 

while(1): 
    print("\nChoose the option you want.")
    print("1. Join membership")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter the number : ")
    match choice: # 회원가입 반복문
        case '1':
            while 1:
                print("\nChoose your User Type. ")
                print("1. Manager")
                print("2. Student")
                print("3. Go back")
                Type = input("Enter the number : ")
                match Type: #Manager로 회원가입
                    case '1':
                        Type = "Manager"
                        CheckNum = input("Enter the Manager check number : ")
                        if Manager.Check(CheckNum) == CheckNum : pass # 맞으면 Manager로 설정
                        else : continue     #틀리면 다시 반복문
                    case '2' :    # Student로 회원가입
                        Type = "Student"
                        pass
                    case '3' : break # 첫페이지로 이동
                    case _: # Option에 없는 수 입력 : Error 
                        print("2-This option is not available. Please enter the available number.\n")
                        continue
                while 1 : # 아이디 설정
                    ID = input("Enter your new ID : ")
                    if ID in UserList : #입력받은 ID가 UserList의 key(=ID)에 존재하는 경우
                        print("This Identifier is exist. Please create another ID.\n")
                        continue # 다시 아이디 설정
                    else : break 
                Password = input("Enter your new Password : ")
                UserList[ID] = {Password : Type}
                #### + def(Type구분) : Type구분해서 사용자 structure 생성해주는 함수
                print("\n*** Welcome to Ajou University! ****\n*** We return to the first Page. ***\n")
                break # 첫페이지로 이동
        case '2': #Login 아이디중복X
            while 1 : 
                GobackCheck = 0
                ID = input("Enter your ID : ")        
                if(ID in UserList): break
                else : 
                    print("\nThere is no User with this ID.\n")
                    GobackCheck = input("1. Retry\n2. Go back\nEnter : ")
                    if GobackCheck == '1' : continue
                    else : break
            if GobackCheck == '2' : continue
            else : pass

            while 1 : 
                Password = input("Enter your Password : ")
                if(Password in UserList[ID].keys()): break
                else :
                    print("Wrong password.\n")
                    GobackCheck = input("1. Retry\n2. Go back\nEnter : ")
                    if GobackCheck == '1' : continue
                    else : break
            if GobackCheck == '2' : continue
            else : pass

            print("Login success.\n")
            GwamokShower()
        

            if UserList[ID][Password] == "Manager" :
                managerOption = 0
                while 1:
                    if ManagerChoice.Manegerchoice() == 4 : break
                    else : continue  
            else : # UserList[ID][Password] == "Student" 
                GwamokCaller()
        case '3': #Exit
             exit()
        case _: #Wrong Choice
             print("\n1-This option is not available. Please enter the available number.")
             continue
