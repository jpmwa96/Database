#this command will import the sql3 system that we will be using to create and manupulate the datebase
import sqlite3
from tkinter import *
#from PIL import ImageTk, Image

# creating the connection from tha database to the python file
#this line could also create a database with the given name if there is not one already.
# "conn" is the abreviation of connection therfore we will be using in order to make the code flow faster

conn= sqlite3.connect('quetion_bank.db')

# in this line we will greate a abreviation for the cursor which is used to call executable action
# we will be using "c" as a abreviation of cursor

c= conn.cursor()

# the follwing line are used to create tables and set their properties.

#--------------------------------------- MODULE TABLE--------------------------------

# this table will be used to store the modules names and modules ID
# the primary key used were will be module_id

# c.execute(""" CREATE TABLE module(
#     module_id INTERGER PRIMARY KEY,
#     module_name TEXT      
#     )""")

#THIS PREVIUOUS LINE OF CODE HAVE BEEN COMMENTED OUT AS IT ONLY CAN CREATE THE TABLE ONCE.

#---------------------------------------QUESTION TABLE---------------------------------

# this table will be used to store the question in relation to modules and will contain 
# question id(pk), module id(fk), answer id(fk) and the question itself.

# c.execute(""" CREATE TABLE questions(
#     question_id INTERGER PRIMARY KEY,
#     quetion TEXT,
#     answer_id INTERGER, 
#     module_id INTERGER,
#     FOREIGN KEY (answer_id) REFERENCES answers(answer_id),
#     FOREIGN KEY (module_id) REFERENCES module(module_id)
# )""")

#THIS PREVIUOUS LINE OF CODE HAVE BEEN COMMENTED OUT AS IT ONLY CAN CREATE THE TABLE ONCE.

#---------------------------------------ANSWER TABLE---------------------------------

# this table will be used to store the answer in relation to modules and will contain 
# answer id(pk), module id(fk), question id(fk) and the answer itself.

# c.execute(""" CREATE TABLE answers(
#     answer_id INTERGER PRIMARY KEY,
#     answer TEXT,
#     question_id INTERGER, 
#     module_id INTERGER,
#     FOREIGN KEY (question_id) REFERENCES questions(question_id),
#     FOREIGN KEY (module_id) REFERENCES module(module_id)
# )""")

#THIS PREVIUOUS LINE OF CODE HAVE BEEN COMMENTED OUT AS IT ONLY CAN CREATE THE TABLE ONCE.

#-----------------------------------------SCORE TABLE------------------------------------

#This table will store all tha ttemps and their score and that will be related to ....
#...each student ID

# c.execute(""" CREATE TABLE scores(
#     attempt_id INTERGER PRIMARY KEY,
#     student_id INTERGER,
#     score INTEGER,
#     module_id INTEGER,
#     FOREIGN KEY (module_id) REFERENCES module(module_id)
# )""")

#THIS PREVIUOUS LINE OF CODE HAVE BEEN COMMENTED OUT AS IT ONLY CAN CREATE THE TABLE ONCE.

#-----------------------------------------END OF TABLES------------------------------

#The folliwng lines have tye function of commiting any command that came.....
#....before and closing the connection.


#--------------------------------------CREATING THE GUI-------------------------------
root=Tk()
root.title('QuizTime')
root.iconbitmap('C:/Users/pedro/Desktop/python/sqlite/gre_minilogo.ico')
root.geometry("700x700")

#------------------------------------CREATINF THE FRAME----------------------

#creating a main frame where all the pages are going to be hold






f_name= Entry(root, width=60)
f_name.grid(row=0, column=0, padx=50)

conn.commit()

conn.close()

root.mainloop()