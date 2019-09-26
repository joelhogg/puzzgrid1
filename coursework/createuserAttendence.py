from tkinter import *
import sqlite3 #Used for interacting with SQLite database

# Class for the main application frame
class Application(Frame):
    # Constructor
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    # Set up the form, called by the constructor
    def create_widgets(self):
        # create label for Username      
        self.lblUserID = Label(self, text = "UserID: ")
        self.lblUserID.grid(row = 1, column = 0, sticky = W)

        # create entry widget to accept Username      
        self.entUserID = Entry(self)
        self.entUserID.grid(row = 1, column = 1, sticky = W)

        # create label for password      
        self.lblName = Label(self, text = "Name: ")
        self.lblName.grid(row = 2, column = 0, sticky = W)


        # create entry widget to accept password      
        self.entName = Entry(self)
        self.entName.grid(row = 2, column = 1, sticky = W)

        # create label for    
        self.lblStatus = Label(self, text = "Status: ")
        self.lblStatus.grid(row = 3, column = 0, sticky = W)


        # create entry widget to accept     
        self.entStatus = Entry(self)
        self.entStatus.grid(row = 3, column = 1, sticky = W)

        # create label for    
        self.lblDateTime = Label(self, text = "DateTime: ")
        self.lblDateTime.grid(row = 4, column = 0, sticky = W)


        # create entry widget to accept     
        self.entDateTime = Entry(self)
        self.entDateTime.grid(row = 4, column = 1, sticky = W)

        # create submit button
        self.btnSubmit = Button(self, text = "Submit", command = self.submit)
        self.btnSubmit.grid(row = 6, column = 0, sticky = W)

        # create view all users button
##        self.btnViewAll = Button(self, text = "View All Users", command = self.viewAllUsers)
##        self.btnViewAll.grid(row = 5, column = 1, sticky = W)
##
##        # create text widget to display all users
##        self.txtDisplay = Text(self, width = 40, height = 5, wrap = WORD)
##        self.txtDisplay.grid(row = 6, pady = 2, column = 0, columnspan = 2, sticky = W)

    # Function to insert new user details into the database
    # Called when the submit button is pressed
    def submit(self):
        vUserID=self.entUserID.get()
        vName=self.entName.get()
        vStatus=self.entStatus.get()
        vDateTime=self.entDateTime.get()
            
##        namelist = conn.execute("SELECT username FROM tblUsers;")
##        vAllUsers = []
##        for user in namelist:
##            vAllUsers.append(user[0])
##            
##        if (vUsername in vAllUsers):
##            print("Username already exists")
##            return None

        # Store these details in the tblUsers table in our database
        conn.execute("INSERT INTO tblUserAttendence (UserID, Name, Status, DateTime) \
                        VALUES (?,?,?,?)",(vUserID, vName, vStatus, vDateTime));

        conn.commit() # Commit the transaction
        conn.close()

        # Show Confirmation message
        #messagebox.showinfo("Success!", "New User Created\n\nUsername: " + vUsername + "\nPassword: " + vPassword)
        print("Sucsess!")
        self.entUserID.delete(0, END) # Clear the Username field
        self.entName.delete(0, END) # Clear the Password field
        self.entStatus.delete(0, END) # Clear the Password field
        self.entDateTime.delete(0, END) #clear datetime feild


    # Function to retrieve all users from the database
    # Called when the view all button is pressed


# main
root = Tk()
root.title("Create Users")
root.geometry("200x120")

#Open a connection to the database
#This will create a new database in the current dir if it doesnt exist
conn = sqlite3.connect('AttendenceRegister.db')

#Create the users table.
conn.execute('''CREATE TABLE IF NOT EXISTS tblUserAttendence
      (
          UserID        INTEGER PRIMARY KEY     ,
          Name          TEXT            NOT NULL,
          Status        TEXT            NOT NULL,
          DateTime      TEXT            NOT NULL
       );''')
conn.commit() # Commit the transaction

app = Application(root)

root.mainloop()

conn.close() # Close the connection to the database
