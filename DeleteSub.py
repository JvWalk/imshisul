import numpy as np
import GwamokCaller
import GwamokChanger

#GwamokCaller.gwamok

#과목 띄우기 구현

def ask():
	print('what class do you want to delete?')
	print('(you can abort by typing \'k\')')
	keyword = input('search by class number : ')
	gumsek = GwamokCaller.gwamok[:,:1]
	if keyword in gumsek :
		loca = np.where(gumsek == keyword)
		locainint=int(loca[0])
		print(locainint)
		print('\nfound',keyword,'!')
		print( 'is', GwamokCaller.gwamok[locainint,:],'the right class?\n')
		isitright=input('type y for\'yes\'\n')
		if isitright == 'y':
			slice1 = GwamokCaller.gwamok[:locainint,:]
			slice2 = GwamokCaller.gwamok[locainint+1:,:]
			deleted = np.concatenate([slice1,slice2])
			GwamokChanger.all(deleted)
			print('succesfully deleted!')
			a = input('if you want to delete more, type y\n')
			if a == 'y' :
				return 1
			else :
				return 0
		else :
			print('wrong input! try again') 
			return 1
	elif keyword == 'k' :
		return 0
	else : 
		print('\ncouldn\'t locate class... please try again\n' ) 
		return 1
# def gumsekjung():
# 	if 

