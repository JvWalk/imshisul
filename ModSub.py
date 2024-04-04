import numpy as np
import GwamokCaller
import GwamokChanger


def ask():
	print('what class do you want to modify?')
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
                    print('what do you want to change?')
                    what = input('number: 1, name : 2, credit:3, junpil: 4,  time: 5, place : 6\n')
                    changing = GwamokCaller.gwamok
                    match what:
                        case '1':
                            how = input('how do you want to change?\n')
                            changing[locainint,0] = how
                            GwamokChanger.all(changing)
                            
                        case '2':
                            how = input('how do you want to change?')
                            changing[locainint,1] = how
                            GwamokChanger.all(changing)
                        case '3':
                            how = input('how do you want to change?')
                            changing[locainint,2] = how
                            GwamokChanger.all(changing)
                        case '4':
                            how = input('how do you want to change?')
                            changing[locainint,3] = how
                            GwamokChanger.all(changing)
                        case '5':
                            how = input('how do you want to change?')
                            changing[locainint,4] = how
                            GwamokChanger.all(changing)
                        case '6':
                            how = input('how do you want to change?')
                            changing[locainint,5] = how
                            GwamokChanger.all(changing)
                        case _:
                                
                            print("\nThis option is not available. Please enter the available number.")

                    print('succesfully changed!')
                    a = input('if you want to delete more, type y\n')
                    if a == 'y' :
                        return 1
                    else :
                        return 0
	elif keyword == 'k' :
		return 0
	else : 
		print('\ncouldn\'t locate class... please try again\n' ) 
		return 1
