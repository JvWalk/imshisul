import numpy as np
import AddSub
import DeleteSub
import ModSub
import GwamokShower

def Manegerchoice():
    print("\nChoose the Option.")
    print("1. Add subject")
    print("2. Delete subject")
    print("3. Modify subject")
    print("4. Exit")
    managerOption = input("Enter the number : ")
    match managerOption :
        case '1':
            while (1) :
                GwamokShower.popup.update_idletasks()
                GwamokShower.popup.update()
                AddSub.classno()
                AddSub.name()
                AddSub.pilsu()
                AddSub.hakjum()
                AddSub.time()
                AddSub.room()
                AddSub.add()
                more = input('Complete! For adding more subject, Enter \'m\'\n')
                if more == 'm':
                    continue
                else :
                    break
        case '2':
            while (1) :
                a = DeleteSub.ask()
                if a != 1:
                    break
        case '3':
            while (1) :
                a = ModSub.ask()
                if a != 1:
                        break
        case '4':
            exit()
        case _:
            print("\nThis option is not available. Please enter the available number.")
##GwamokShower.showing()
##thread1 = threading.Thread(GwamokShower.popup.mainloop())
##thread1.daemon = True
##thread1.start()

Manegerchoice()



