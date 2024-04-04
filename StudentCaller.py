import numpy as np

while (1) : 
print('you are student class. choose what action you will make')
print('type 1 to add class, type 2 to delete class, type 3 to see what class you\'ve added')
	action = input('')
	match action : 
		case '1':
			Addclass()
		case '2' :
			DeleteClass()
		case '3' :
			SeeSugang()
		case _: 
			print('wrong input! please try again...')

#time thing we have to consider
