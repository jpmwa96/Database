#--------------------------INTEFARCE FOR QUESTIONAIRE----------------------------------------
#THIS CODE IS RESPOSIBLE FOR ALL GUI OF THE PROGRAM
# this line will be importing all the extesion and files that will be used in this code
from tkinter import *
from Question_data_bank import *
from PIL import ImageTk,Image
################################CREATING THE PRIMA WINDOWN #################################################

root= Tk()
root.title("Question")
root.iconbitmap('users/jpmwa/onedrive/universityofgreenwich/sql3/python/sqlite/gre_minilogo.ico')
#givng a lable to the windown
primarylable= Label(root, text="QuizMania")

#position of the lable on the windown
primarylable.grid(row=0, column=0)
#click function

def editclick():
    editlable= Label(root, text="Edit")
    editlable.grid(row=0, column=0)
def quizclick():
    quizlable= Label(root, text="Quiz")
    quizlable.grid(row=0, column=0)
def resultclick():
    resultlable= Label(root, text="Result")
    resultlable.grid(row=0, column=0)
    # 
    
#creating the buttons forfor the main windown
editbuttom=Button(root, text="Edit" ,command=editclick)
editbuttom.grid(row=5, column=5)

quizbutton=Button(root, text="Quiz",command=quizclick)
quizbutton.grid(row=10, column=5)

resultbutton=Button(root, text="Result",command=resultclick)
resultbutton.grid(row=20, column=5)

exitbutton=Button(root, text="Exit",command=root.quit)
exitbutton.grid(row=45, column=5)



root=mainloop()