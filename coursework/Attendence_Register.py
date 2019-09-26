from tkinter import *
import sqlite3

#note there is a seperate py program to input into db table
class Table(Frame): #height=no. of columns width=rows[database function must be first ran]
    def __init__(self,master,height,bigarray):
        #width += 1 #have to use up one row for Subtitles
        width = (len(bigarray[0])+1)
        super(Table,self).__init__(master)
        self.grid()
        self.create_widgets(height,width) #runs function to create textboxes for table
        self.insert_table(bigarray)

    def create_widgets(self,height,width):
        self.widget_loc = {} #store each widget here
        #create a widget for width, height
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = Entry(root, text="")#state='disabed' stops input
                b.grid(column=i, row=j)#organises widget to grid
                self.widget_loc[i,j] = b #stores widget in dictionary

        #retreives top row of widgets from dict
        subtitle_1 = self.widget_loc[(0,0)] 
        subtitle_2 = self.widget_loc[(1,0)]
        subtitle_3 = self.widget_loc[(2,0)]

        #changes text field of top row to match design spec
        subtitle_1.insert(0,"Name")
        subtitle_2.insert(0,"Status")
        subtitle_3.insert(0,"Date/Time")

    def insert_table(self,bigarray): #inserts each item from array to its place in tbl
        for i in range(0,3):
            for j in range(len(bigarray[0])):
                k = self.widget_loc[i,(j+1)]#j+1 as first row filled
                k.insert(0,(bigarray[i][j]))

    
    

def database():
    conn = sqlite3.connect("AttendenceRegister.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS tblUserAttendence
      (
          UserID        INTEGER PRIMARY KEY     ,
          Name          TEXT            NOT NULL,
          Status        TEXT            NOT NULL,
          DateTime      INTEGER         NOT NULL
       );''')
    conn.commit()

    #retreive all items out of database table
    c = conn.cursor
    #conn.execute("SELECT Name FROM tblUserAttendence")
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    names = c.execute("SELECT Name From tblUserAttendence")
    namelist = []
    for row in names:
        namelist.append(row)
        
    statuses = c.execute("SELECT Status From tblUserAttendence")
    statuslist = []
    for row in statuses:
        statuslist.append(row)
        
    times = c.execute("SELECT DateTime From tblUserAttendence")
    timelist = []
    for row in times:
        timelist.append(row)
        
    UnIDs = c.execute("SELECT UserID From tblUserAttendence")
    UnIDlist = []
    for row in UnIDs:
        UnIDlist.append(row)

    bigarray = [namelist,statuslist,timelist,UnIDlist]
    return bigarray
#main
root= Tk()
root.title("Attendence Regsiter")
dblist = database()
table = Table(root,3,dblist)
root.mainloop()


#todo:
#
#-make tkinter part as a class/function X
#do sqlite3 part to read database into an array or simlarX
#function to read data into tkniter table (can be function of tkinter section class)X
#automaticly use correct number of rows
