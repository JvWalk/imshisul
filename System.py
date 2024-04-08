import hashlib
import csv
import numpy as np
import Manager


def checkID(ID):
    with open('userList.csv','r') as f:
        user = csv.DictReader(f) #딕셔너리 형태로 파일 읽어옴
        for i in user:
            if ID in i['ID'] : return True #ID key에 해당 value있으면 True
        return False
    
def getType(ID):
    with open('userList.csv','r') as f:
        user = csv.reader(f)
        for i in user:
            if ID in i[0]: return i[1]

def checkPW(ID, Password):  #비밀번호 확인
    hash = hashlib.sha256()
    hash.update(Password.encode('utf-8'))
    with open('userList.csv','r') as f:
        user = csv.reader(f)
        for i in user:
            if ID in i[0]:
                if hash.hexdigest() in i[2]: return True
        return False



def addUser(ID, Type, Password): #유저 등록
    with open('userList.csv','a',newline='') as f:
        hash = hashlib.sha256()     #sha256으로 해싱
        hash.update(Password.encode('utf-8')) 
        user = csv.writer(f)    #쓰기버전으로 읽음
        user.writerow([ID, Type, hash.hexdigest()]) #정보 저장



def membership():
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
                if Manager.Check(CheckNum) == CheckNum : break # 맞으면 Manager로 설정
                else : continue     #틀리면 다시 반복문
            case '2' :    # Student로 회원가입
                Type = "Student"
                break
            case '3' : return # 첫페이지로 이동
            case _: # Option에 없는 수 입력 : Error 
                print("2-This option is not available. Please enter the available number.\n")
                continue
    while 1 : # 아이디 설정
            ID = input("Enter your new ID : ")
            if checkID(ID) : #입력받은 ID가 UserList의 key(=ID)에 존재하는 경우
                print("This Identifier is exist. Please create another ID.\n")
                continue # 다시 아이디 설정
            else : break 
    Password = input("Enter your new Password : ")
    addUser(ID, Type, Password)
    print("\n*** Welcome to Ajou University! ****\n*** We return to the first Page. ***\n")

def login():
    while 1 : 
        GobackCheck = 0
        ID = input("Enter your ID : ")        
        if checkID(ID): break
        else : 
            print("\nThere is no User with this ID.\n")
            GobackCheck = input("1. Retry\n2. Go back\nEnter : ")
            if GobackCheck == '1' :  continue
            elif GobackCheck == '2' :  break
            else : continue
    if GobackCheck == '1' : return ID == '', Password == ''
    else : pass
    while 1 : 
        Password = input("Enter your Password : ")
        if checkPW(ID, Password) : break
        else :
            print("Wrong password.\n")
            GobackCheck = input("1. Retry\n2. Go back\nEnter : ")
            if GobackCheck == '1' : continue
            elif GobackCheck == '2' :  break
            else : continue
    if GobackCheck == '1' : return
    else : pass
    print("Login success.\n")
    return ID, Password