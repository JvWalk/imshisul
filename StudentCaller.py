import numpy as np
import Student
import time
import datetime

chamkae11 = Student.student('chamkae11')  #아이디 예시(ID = chamkae11)

Timeleft = 300          #사용할수 있는 시간 = 300초

while (1) : 
    Starttime = time.time()  #시작 시간
    if Timeleft < 0 :   #남은 시간이 없을 시
        print('Time out! please log in again.\n')
        break               #로그인 화면으로 돌아감

    print('You are student class. choose what action you will make')
    print('Type 1 to add class, type 2 to delete class, type 3 to see what class you\'ve added:') #student 수강신청 화면
    print('(Time left untill time out : ',round(Timeleft, 1),' sec)')
    action = input('')
    
    match action :              #input 확인
        case '1':               #수강신청 
            print('What class are you adding?')
            print('(Type a to abort)')

            cl_num = input('')  #과목 번호 확인
            if cl_num != 'a' :
                    Student.student.Addclass(chamkae11,cl_num)          #수강신청 함수 호출
            Timeleft = Timeleft + Starttime- time.time()        #걸린 시간 저장
            
        case '2' :              #수강취소
            print('What class are you deleting?')
            print('(Type a to abort :)')
            cl_num = input('')  #과목 번호 확인
            if cl_num != 'a' :
                    Student.student.Deleteclass(chamkae11,cl_num)  #수강정정 함수 호출
            Timeleft = Timeleft + Starttime- time.time()        #걸린 시간 저장
            
        case '3' :
            schedule = Student.student.Showschedule(chamkae11)  #스케줄표 열어주는 함수 호출
            Timeleft = Timeleft + Starttime- time.time()        #스케줄표를 닫을 때까지 걸린 시간 저장
            print('\n')
        case _: 
            print('Wrong input! please try again...\n')         #잘못된 입력시 에러
            Timeleft = Timeleft + Starttime- time.time()

