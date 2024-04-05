import numpy as np

while (1) : 
print('you are student class. choose what action you will make')
print('type 1 to add class, type 2 to delete class, type 3 to see what class you\'ve added')
	action = input('')
	match action : 
		case '1':
			print('What class are you trying to add?')
			print('(If you didn\'t scheduled 4 or more required class, we notice you that your call can be rejected)')
			classnum = input('')
			aa = Addclass(classnum)
			if aa is 1 : 
				break
		case '2' :
			DeleteClass()
		case '3' :
			SeeSugang()
		case _: 
			print('wrong input! please try again...')

#time thing we have to consider
