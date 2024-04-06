import numpy as np
import csv
#import GwamokCaller


Newsub = []
day1=int
day2=int
time1=int
time2=int
grade=int
roomnum=int
def classno():
        i = input("Enter class number : ")
        Newsub.insert(0, i)
def name():
        i = input("Enter class name : ")
        Newsub.insert(1, i)
def pilsu():
        while 1 :
                # i = input("Is it major pilsu? answer y for 'yes', n for 'no'")
                i = input("\nChoose the class type\n1.Required\n2.Elective\nEnter the number : ")
                if i == '1' :
                        Newsub.insert(2, 'Required')
                        break
                elif i == '2' :
                        Newsub.insert(2, 'Elective')
                        break
                else : 
                        print('wrong input! try again')
                        continue

def hakjum():
        i = input("Enter class credit:")
        Newsub.insert(3, i)

def time():
        d1 = input("\nChoose the day of the first class.\n1. Mon    2. Tue    3. Wed    4. Thu    5. Fri\nEnter the number : ")
        t1 = input("\nChoose the time of the class.\n1. A | 9:00\n2. B | 10:00\n3. C | 11:00\n4. D | 12:00\n5. E | 13:00\n6. F | 14:00\nEnter the number : ")
        day1, time1 = tradeTime(d1, t1)
        hour1 = input("\nChoose the hour class will take place.\n1. Theory class : 1 hour \n2. Experimental class : 4 hour \nEnter the number : ")
        d2 = input("\nChoose the day of the second class.\n1. Mon    2. Tue    3. Wed    4. Thu    5. Fri\nEnter the number : ")
        t2 = input("\nChoose the time of the class.\n1. A | 9:00\n2. B | 10:00\n3. C | 11:00\n4. D | 12:00\n5. E | 13:00\n6. F | 14:00\nEnter the number : ")
        day2, time2 = tradeTime(d2, t2)
        hour2 = input("\nChoose the hour class will take place.\n1. Theory class : 1 hour \n2. Experimental class : 4 hour \nEnter the number : ")
        Newsub.insert(4, day1+'#'+time1+hour1+'#'+day2+'#'+time2+hour2) #join 함수 활용

def room():
        gwan = input("Enter hall : ")
        roomnum = input("Enter room number : ")
		#if 시간과 강의실 중복검사
        Newsub.insert(5, gwan+'#'+roomnum) #join 함수 활용
        
def add():
        f = open("basics.txt",'a')
        for i in range(6) :
                adding = Newsub[i]
                f.write(adding)
                f.write('\t')

        f.write('\n')
        f.close()

def tradeTime(day, time):
        match day:
                case '1': day = 'Mon'
                case '2': day = 'Tue'
                case '3': day = 'Wed'
                case '4': day = 'Thu'
                case '5': day = 'Fri'
        match time:
                case '1': time = 'A'
                case '2': time = 'B'
                case '3': time = 'C'
                case '4': time = 'D'
                case '5': time = 'E'
                case '6': time = 'F'
        return day, time
