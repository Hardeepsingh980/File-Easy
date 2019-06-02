from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import shutil


class File_easy:

    def sort_main(self):
        dir_ = fd.askdirectory(initialdir='D:\\',title='Select Directory')

        if dir_ == '':
            return True

        music_ex = ['mp3','wav']
        video_ex = ['mp4','mkv']
        doc_ex = ['py','txt']
        exe_ex = ['exe']
        img_ex = ['jpg','jpeg','png']

        dir_files = os.listdir(dir_)

        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    try:
                        os.mkdir(f'{dir_}\\Music')
                    except FileExistsError:
                        pass
                    
                    src = dir_+'\\'+file

                    shutil.move(src,f'{dir_}\\Music')

            for ex in video_ex:
                if exten == ex:
                    try:
                        os.mkdir(f'{dir_}\\Video')
                    except FileExistsError:
                        pass
                    
                    src = dir_+'\\'+file

                    shutil.move(src,f'{dir_}\\Video')

            for ex in img_ex:
                if exten == ex:
                    try:
                        os.mkdir(f'{dir_}\\Images')
                    except FileExistsError:
                        pass
                    
                    src = dir_+'\\'+file

                    shutil.move(src,f'{dir_}\\Images')

            for ex in doc_ex:
                if exten == ex:
                    try:
                        os.mkdir(f'{dir_}\\Documents')
                    except FileExistsError:
                        pass
                    
                    src = dir_+'\\'+file

                    shutil.move(src,f'{dir_}\\Documents')

            for ex in exe_ex:
                if exten == ex:
                    try:
                        os.mkdir(f'{dir_}\\Exe_files')
                    except FileExistsError:
                        pass
                    
                    src = dir_+'\\'+file

                    shutil.move(src,f'{dir_}\\Exe_files')
                        
                    
                    
        message = mb.askquestion('Done','Sorting Process Is Complete.\n'+'Click The Yes Button To Check The Folder.')
        if message == 'yes':
            os.startfile(dir_)

        

    def del_dup(self):
        dir_ = fd.askdirectory(initialdir='D:\\',title='Select Directory')

        if dir_ == '':
            return True
        
        os.chdir('D:\\')

        files = []

        files_2 = []

        to_del = []
        
        drive = dir_

        main = os.listdir(f'{drive}\\')
        for i in main:

            try:
                sub = os.listdir(f'{drive}\\{i}')
                for j in sub:

                    try:
                        sub_2 = os.listdir(f'{drive}\\{i}\\{j}')                
                        for k in sub_2:

                            try:
                                sub_3 = os.listdir(f'{drive}\\{i}\\{j}\\{k}')
                                for m in sub_3:

                                    try:
                                        sub_4 = os.listdir(f'{drive}\\{i}\\{j}\\{k}\\{m}')
                                    except:

                                        files.append(f'{drive}\\{i}\\{j}\\{k}\\{m}')        
                                        pass
                            except:

                                files.append(f'{drive}\\{i}\\{j}\\{k}')        
                                pass
                            
                    except:

                        files.append(f'{drive}\\{i}\\{j}')        
                        pass
                        
                
            except:

                files.append(f'{drive}\\{i}')        
                pass


            




        for i in files:
            n = i.split('\\')
            new = n[-1]
            if new not in files_2:
                files_2.append(new)
            else:
                 to_del.append(i)

        str_ = []
        if len(to_del) != 0: 
            for i in to_del:            
                str_.append(i+'\n')

            message = mb.askquestion('Confirm', 'Duplicate Find At : \n\n'+''.join(str_)+'\nDo You Want To Delete All The Files.')

            if message == 'yes':
                for i in to_del:
                    os.remove(i)
                mb.showinfo('Done', 'Duplicates Successfully Removed\n'+str(len(to_del))+' Files Were Removed.')
                    
            else:
                mb.showinfo('Done','You Choosed No.\n0 Files Were Removed.')
        else:
            mb.showinfo('Done','Scan Complete.\n'+'No Duplicated Were Found In Selected Directory.')





    def home_func(self):
        header.configure(text='Welcome...',font=('Georgia',30))
        header.place(x=180,y=80)
        caption1.configure(text='Select The Options\n At Left To Perform A Task.',font=('Georgia',20))
        caption1.place(x=180,y=180)
        button.place(x=10000,y=1000)


    def delete_dup_func(self):
        header.configure(text='Delete Duplicate',font=('Georgia',20))
        header.place(x=180,y=80)
        caption1.configure(text='Choose The Directory\n Where You Want To  Search For Duplicates.',font=('georgia',12))
        caption1.place(x=160,y=150)
        button.configure(text='Choose Directory',command=self.del_dup)
        button.place(x=180,y=250)

    def sort_func(self):
        header.configure(text='Sort',font=('Georgia',30))
        header.place(x=180,y=80)
        caption1.configure(text='Choose The Directory\n Where You Want To  Sort The Files.',font=('georgia',12))
        caption1.place(x=160,y=150)
        button.configure(text='Choose Directory',command=self.sort_main)
        button.place(x=180,y=250)

    def help_func(self):
        header.configure(text='Help',font=('Georgia',30))
        header.place(x=180,y=60)
        caption1.configure(text='This Application Have Two Features : \n\nDelete Duplicate : This Search For The Duplicate Files\n In Your PC And Help You To Clear Them.\n\nSort:This Helps You To Sort Your Different Types Of \n Files Into Different Folders. ',font=('georgia',12))
        caption1.place(x=140,y=130)
        button.place(x=10000,y=1000)

    def about_func(self):
        header.configure(text='About',font=('Georgia',30))
        header.place(x=180,y=80)
        caption1.configure(text='This Application Was Created By Hardeep Singh.\n He Created This For Personal Use But Later\n On A Demand This Was Published To Public.\n This Application Was Created Using Python.\n This Was One Of The Project Of Hardeep Singh.\nContact Us At: 9803588671',font=('georgia',12))
        caption1.place(x=160,y=150)
        button.place(x=23000,y=25000)

    
    def __init__(self):
        win = Tk()
        win.geometry('550x310+250+200')
        win.title('File Easy')
        win.resizable(0,0)
        win.iconbitmap('file.ico')

        Label(win, text='File Easy',bg='green',fg='white',font=('arial black',26),width=30).pack()
        
        Label(win,bg='green',height=30,width=18).place(x=0,y=0)

        img = PhotoImage(file='file.png')
        
        Label(win,bg='red',height=7,width=10).place(x=450,y=0)

        Button(win,image=img,bg='red',bd=0,command=self.about_func).place(x=452,y=40)

        

        Button(win,bg='green',fg='white',text='  Home',font=('arial black',14),bd=0,command=self.home_func).place(x=10,y=60)

        Button(win,bg='green',fg='white',text='Delete\nDuplicates',font=('arial black',14),bd=0,command=self.delete_dup_func).place(x=0,y=100)

        Button(win,bg='green',fg='white',text='Sort Files',font=('arial black',14),bd=0,command=self.sort_func).place(x=0,y=180)

        Button(win,bg='green',fg='white',text=' Help',font=('arial black',14),bd=0,command=self.help_func).place(x=5,y=230)

        Button(win,bg='green',fg='white',text=' About',font=('arial black',14),command=self.about_func,bd=0).place(x=5,y=270)

        global copyright_
        copyright_ = Label(win, bg='white',text='Copyright Belong\n To Hardeep Singh.',font=('Courier',8)).place(x=420,y=270)

        global header
        header = Label(win, text='Welcome...',font=('Georgia',30))
        header.place(x=180,y=80)

        global caption1
        caption1 = Label(win, text='Select The Options\n At Left To Perform A Task.',font=('Georgia',20))
        caption1.place(x=180,y=180)

        global button
        button = Button(win, text='',font=('Georgia',20),bd=0,bg='green',fg='white')
                
        win.mainloop()



file_object = File_easy()
