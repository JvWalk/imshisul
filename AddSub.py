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
        i = input("enter class number:")
        Newsub.insert(0, i)
def name():
        i = input("enter class name:")
        Newsub.insert(1, i)
def pilsu():
        while 1 :
                i = input("is it major pilsu? answer y for 'yes', n for 'no'")
                if i == 'y' :
                        Newsub.insert(2, 'Required')
                        break
                elif i == 'n' :
                        Newsub.insert(2, 'Elective')
                        break
                else : 
                        print('wrong input! try again')
                        continue

def hakjum():
        i = input("enter class credit:")
        Newsub.insert(3, i)

def time():
        day1 = input("enter day1 :")
        time1 = input("enter time1 :")
        day2 = input("enter day2 :")
        time2 = input("enter time2 :")
        Newsub.insert(4, day1+'#'+time1+'#'+day2+'#'+time2)

def room():
        gwan = input("enter hall :")
        roomnum = input("enter room number :")
		#if 시간과 강의실 중복검사
        Newsub.insert(5, gwan+'#'+roomnum)
        
def add():
	f = open("basics.txt",'a')
	f.write('\n')
	for i in range(6) :
                idk = Newsub[i]
                f.write(idk)
                f.write('\t')
	f.close()

