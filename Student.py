import numpy as np
import GwamokCaller

class Student:

#need time.time

    def __init__(self, ID):
        self.ID = ID
        #개인 id 정보 txt에 넣기
        self.Mysubject = RecallSub(ID)

    def Addclass(self, Classnum):

        gumsek = GwamokCaller.gwamok[:,0]
        time = GwamokCaller.gwamok[:,4]

        #check if user has 4 junpi
        #if not is this class junpil?
        #if not reject by return 1
        #or else
        if Classnum in gumsek :
            datetonum = []
            timetonum = []
            arr1 = []
            loca = np.where(gumsek == Classnum)
            arr2 = time[int(loca[0])].split('#')
            date = arr2[::2]
            arr3 = arr2[1::2]
            for i in range(len(arr3)):
                arr1.extend(list(arr3[i]))
            startingtime = arr1[::2]
            howlong = arr1[1::2]
            for i in date:
                a = i.replace('Mon','1').replace('Tue','2').replace('Wed','3').replace('Thu','4').replace('Fri','5')
                datetonum.append(a)
            for i in startingtime:
                a = i.replace('A','1').replace('B','2').replace('C','3').replace('D','4').replace('E','5').replace('F','6')
                timetonum.append(a)

            Myschedule = Makeschedule()

            for i in range(len(datetonum)) :
                if Myschedule[int(timetonum[i])-1][int(datetonum[i])-1] != 0 : 
                    print('Error! You have another class for the time of class you attending to.')
                    return 1
            print('sugang complete!')
                #add to mysubject
        else :
            print('There\'s no class that matches your request. Please try again.')
            return 1    



        # Classtime = []
        # gumsek = GwamokCaller.gwamok[:,5]
        # for line in arr
        #     Classtime = line.split('#')
        # if Classnum in gumsek :
        #     self.Mysubject

    def Deleteclass():

        #check if you have callin gwamok
        #if you have it, erase then save
        
    def Seeclass():
        Schedulelist = Makeschedule()
        #schedule pop-up

    def Makeschedule(self): 
        Classnum = self.Mysubject[:,0]
        Schedulelist = np.zeros([9,5])
    
        time = GwamokCaller.gwamok[:,4]
        gumsek = GwamokCaller.gwamok[:,0]

        for subcount in range(len(Classnum)) :
            datetonum = []
            timetonum = []
            arr1 = []
            loca = np.where(gumsek == Classnum[subcount])
            arr2 = time[int(loca[0])].split('#')
            date = arr2[::2]
            arr3 = arr2[1::2]
            for i in range(len(arr3)):
                arr1.extend(list(arr3[i]))
            startingtime = arr1[::2]
            howlong = arr1[1::2]
            for i in date:
                a = i.replace('Mon','1').replace('Tue','2').replace('Wed','3').replace('Thu','4').replace('Fri','5')
                datetonum.append(a)
            for i in startingtime:
                a = i.replace('A','1').replace('B','2').replace('C','3').replace('D','4').replace('E','5').replace('F','6')
                timetonum.append(a)

            for i in range(len(datetonum)) :
                for j in range(int(howlong[i])) :
                    Schedulelist[int(timetonum[i])+j-1][int(datetonum[i])-1] = Classnum[subcount]
                    
        return np.array(Schedulelist)