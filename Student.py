import numpy as np
import Subject
import System
import tkinter as tk

class student:

#need time.time

    def __init__(self, ID):
        self.ID = ID
        #개인 id 정보 txt에 넣기
        self.Mysubject = self.RecallSub(ID)
        self.Chonghakjum = self.Hakjumadder()
        self.Junpilnum = self.Junpilchecker()
        
    def RecallSub(self, StudentName) : 
        f = open('Student_schedule/'+StudentName+'.txt', 'r')
        arr = []
        for line in f:
            line = line.strip()
            list= line.split('\t', 6)
            arr.extend([list])
            gwamok = np.array(arr)   
        f.close()
        return gwamok 

    def Hakjumadder(self):
        temp = 0
        hakjum = self.Mysubject [:,3]
        for i in range(len(hakjum)):
            temp = temp + int(hakjum[i])
        return temp

    def Junpilchecker(self):
        junpil = self.Mysubject [:,2]
        countall = np.where(junpil == 'Required')
        return int(len(countall[0]))

    def Addclass(self, Classnum):
        gumsek = Subject.Caller.gwamok[:,0]
        time = Subject.Caller.gwamok[:,4]

        #check if user has 4 junpi
        #if not is this class junpil?
        #if not reject by return 1
        if Classnum in gumsek :
            datetonum = []
            timetonum = []
            
            arr1 = []
            loca = np.where(gumsek == Classnum)
            if self.Junpilnum < 4 and Subject.Caller.gwamok[int(loca[0][0])][2] != 'Required': 
                print('You have to listen at least 4 junpil class first. You now have', self.Junpilnum ,'junpil class.')
                print('Please attend 4 or more junpil first\n')
                return 1
            if self.Chonghakjum + int(Subject.Caller.gwamok[int(loca[0][0])][3]) > 17 : 
                print('Your max credit is 17. You now have', self.Chonghakjum,'.')
                print('Please try again\n')
                return 1
            arr2 = time[int(loca[0][0])].split('#')
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

            Myschedule = self.Makeschedule() # 스케줄이랑 내 스케줄 비교

            for i in range(len(datetonum)) :
                for j in range(int(howlong[i])) :
                    if Myschedule[int(timetonum[i])+j-1][int(datetonum[i])-1] != 0 : 
                        print('Error! You have another class for the time of class you attending to.\n')
                        return 1

            f = open('Student_schedule/'+self.ID+'.txt','a')
            for i in range(6) :
                adding = Subject.Caller.gwamok[(loca[0][0])][i]
                f.write(adding)
                f.write('\t')

            f.write('\n')
            f.close()
            self.Mysubject = self.RecallSub(self.ID)
            self.Junpilnum = self.Junpilchecker()
            self.Chonghakjum = self.Hakjumadder()
            print('sugang complete!\n')
                #add to mysubject
        else :
            print('There\'s no class that matches your request. Please try again.\n')
            return 1    



        # Classtime = []
        # gumsek = GwamokCaller.gwamok[:,5]
        # for line in arr
        #     Classtime = line.split('#')
        # if Classnum in gumsek :
        #     self.Mysubject

    def Deleteclass(self,Classnum): 
        gumsek = self.Mysubject[:,0]
        if Classnum in gumsek :
            loca = np.where(gumsek == Classnum)
            locainint=int(loca[0][0])
            print('\nFound',Classnum,'!')
            print( 'Are you sure you want to drop out?\n')
            print( 'Type y for yes\n')
            TorF = input('')
            if TorF == 'y' : 
                slice1 = self.Mysubject[:locainint,:]
                slice2 = self.Mysubject[locainint+1:,:]
                deleted = np.concatenate([slice1,slice2])
                f = open('Student_schedule/'+self.ID+'.txt', 'w')
                for i in range(deleted.shape[0]):
                    for j in range(deleted.shape[1]):
                        f.write(deleted[i,j])
                        f.write('\t') 
                    f.write('\n')
                f.close()
                print('succesfully deleted!')
                self.Mysubject = self.RecallSub(self.ID)
                self.Chonghakjum = self.Hakjumadder()
                self.Junpilnum = self.Junpilchecker()  

                a = input('if you want to delete more, type y\n')
        else :
            print('There\'s no class that matches your request. Please try again.')
            return 1 


    def Makeschedule(self): #스케줄 만듬
        Classnum = self.Mysubject[:,0]
        Schedulelist = np.zeros([9,5])
        time = self.Mysubject[:,4]
        # gumsek = Subject.Caller.gwamok[:,0]
        for subcount in range(len(Classnum)) :
            datetonum = []
            timetonum = []
            arr1 = []
            # loca = np.where(gumsek == Classnum[subcount])

            arr2 = time[subcount].split('#')
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


    # def Showschedule(self): #스케줄 띄워줌 . ScheduleList

    #     #check if you have callin gwamok
    #     #if you have it, erase then save
    #     Schedulelist = self.Makeschedule()
    #     popup=tk.Tk()
    #     popup.title()
    #     popup.geometry("900x380+100+1")
    #     popup.resizable(False, False)


    #     label = tk.Label(popup, height=1)
    #     show = tk.Label(text="A", width=20, height=2)
    #     show.grid(row=1, column=0)
    #     show = tk.Label(text="B", width=20, height=2)
    #     show.grid(row=2, column=0)
    #     show = tk.Label(text="C", width=20, height=2)
    #     show.grid(row=3, column=0)
    #     show = tk.Label(text="D", width=20, height=2)
    #     show.grid(row=4, column=0)
    #     show = tk.Label(text="E", width=20, height=2)
    #     show.grid(row=5, column=0)
    #     show = tk.Label(text="F", width=20, height=2)
    #     show.grid(row=6, column=0)
    #     show = tk.Label(text="G", width=20, height=2)
    #     show.grid(row=7, column=0)
    #     show = tk.Label(text="H", width=20, height=2)
    #     show.grid(row=8, column=0)
    #     show = tk.Label(text="I", width=20, height=2)
    #     show.grid(row=9, column=0)
    #     show = tk.Label(text="Mon", width=20, height=2)
    #     show.grid(row=0, column=1)
    #     show = tk.Label(text="Tue", width=20, height=2)
    #     show.grid(row=0, column=2)
    #     show = tk.Label(text="Wed", width=20, height=2)
    #     show.grid(row=0, column=3)
    #     show = tk.Label(text="Thu", width=20, height=2)
    #     show.grid(row=0, column=4)
    #     show = tk.Label(text="Fri", width=20, height=2)
    #     show.grid(row=0, column=5)
    #     for i in range(Schedulelist.shape[0]):
    #         for j in range(Schedulelist.shape[1]):
    #             # if Schedulelist[i][j] != 0:
    #             show  = tk.Label(text=int(Schedulelist[i][j]), width=20, height=2)
    #             show.grid(row=i+1, column=j+1)

    #     popup.mainloop()