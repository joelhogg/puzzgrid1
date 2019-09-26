import sys
import sqlite3
import datetime

username = sys.argv[1]
password = sys.argv[2]
statuschange = sys.argv[3]

##if statuschange == "none":
##    print("") #verify username/password
##elif statuschange == "in":
##    print("") #sign in
##elif statuschange == "out":
##    print("") #sign out

#add validation
#username = username.lower() #make it allow numbers
def checkdetails(username, password):
    
    conn = sqlite3.connect("AttendenceRegister.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS tblUserDetails
          (
              UserID        INTEGER PRIMARY KEY     ,
              Username      TEXT            NOT NULL,
              Password      TEXT            NOT NULL
           );''')
    conn.commit()
    cursor = conn.cursor()

    cursor.execute("SELECT Password FROM tblUserDetails WHERE Username='"+username+"'")
    pw = (cursor.fetchall())[0][0]
    conn.close()

    if pw == password:
        return True
    else:
        return False
    

CheckDetails = checkdetails(username,password)
if CheckDetails == True:
    if (statuschange != "none"):
        conn = sqlite3.connect("AttendenceRegister.db")
        conn.execute('''CREATE TABLE IF NOT EXISTS tblUserAttendence
              (
                  UserID        INTEGER PRIMARY KEY     ,
                  Name          TEXT            NOT NULL,
                  Status        TEXT            NOT NULL,
                  DateTime      TEXT            NOT NULL
               );''')
        cursor = conn.cursor()
        now = datetime.datetime.now()
        datetime_now = (str(now.day)+str(now.month)+str((str(now.year))[2:])+str(now.hour)+str(now.minute))
        datetime_now = str(datetime_now)
        try:
            cursor.execute('''UPDATE tblUserAttendence SET Status=?,DateTime=? WHERE Name=?''', (statuschange,datetime_now,username))
            print(1)
        except:
            print("error1")
        conn.commit()
        conn.close()
    elif (statuschange == "none"):
        print(1)

else:
    if (statuschange == "none"):
        print(0)
    else:
        print("error")


    
