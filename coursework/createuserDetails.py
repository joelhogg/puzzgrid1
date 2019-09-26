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
        self.lblUsername = Label(self, text = "Username: ")
        self.lblUsername.grid(row = 2, column = 0, sticky = W)


        # create entry widget to accept password      
        self.entUsername = Entry(self)
        self.entUsername.grid(row = 2, column = 1, sticky = W)

        # create label for    
        self.lblPassword = Label(self, text = "Password: ")
        self.lblPassword.grid(row = 3, column = 0, sticky = W)


        # create entry widget to accept     
        self.entPassword = Entry(self)
        self.entPassword.grid(row = 3, column = 1, sticky = W)


        # create submit button
        self.btnSubmit = Button(self, text = "Submit", command = self.submit)
        self.btnSubmit.grid(row = 5, column = 0, sticky = W)

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
        vUsername=self.entUsername.get()
        vPassword=self.entPassword.get()
            
##        namelist = conn.execute("SELECT username FROM tblUsers;")
##        vAllUsers = []
##        for user in namelist:
##            vAllUsers.append(user[0])
##            
##        if (vUsername in vAllUsers):
##            print("Username already exists")
##            return None

        # Store these details in the tblUsers table in our database
        conn.execute("INSERT INTO tblUserDetails (UserID, Username, Password) \
                        VALUES (?,?,?)",(vUserID, vUsername, vPassword));

        conn.commit() # Commit the transaction
        conn.close()

        # Show Confirmation message
        #messagebox.showinfo("Success!", "New User Created\n\nUsername: " + vUsername + "\nPassword: " + vPassword)
        print("Sucsess!")
        self.entUserID.delete(0, END) # Clear the Username field
        self.entUsername.delete(0, END) # Clear the Password field
        self.entPassword.delete(0, END) # Clear the Password field


    # Function to retrieve all users from the database
    # Called when the view all button is pressed
    def viewAllUsers(self):
        # Retrieve the contents of the tblCustomer table and store to a List var.
        lCustomerDetails = conn.execute("SELECT UserID, Username, Password \
                                            FROM tblUserDetails")

        # Loop through the list and print the contents.
        vAllUsers = ""
        for user in lCustomerDetails:
            vAllUsers = vAllUsers + str(user[0]) + " "
            vAllUsers = vAllUsers + user[1] + " "
            vAllUsers = vAllUsers + user[2] + "\n"
            
        # Update the message box    
        self.txtDisplay.delete(0.0, END)
        self.txtDisplay.insert(0.0, vAllUsers)


# main
root = Tk()
root.title("Create Users")
root.geometry("200x120")

#Open a connection to the database
#This will create a new database in the current dir if it doesnt exist
conn = sqlite3.connect('AttendenceRegister.db')

#Create the users table.
conn.execute('''CREATE TABLE IF NOT EXISTS tblUserDetails
      (
          UserID        INTEGER PRIMARY KEY     ,
          Username      TEXT            NOT NULL,
          Password      TEXT            NOT NULL
       );''')
conn.commit() # Commit the transaction

app = Application(root)

root.mainloop()

conn.close() # Close the connection to the database
