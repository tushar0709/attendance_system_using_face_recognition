#import module from tkinter for UI
from tkinter import *
from playsound import playsound
import os
from datetime import date
#creating instance of TK
root=Tk()

root.configure(background="white")
#root.geometry("300x300")

#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")


def function3():
    os.system("python bug.py")
    playsound('sound.mp3')

def function6():

    root.destroy()

def attend():
    today=date.today()
    strToday = today.strftime('%y-%m-%d')

    os.startfile("C:/Users/DELL/PycharmProjects/Mini_project_SDL/attendance_sheet/"+ strToday + ".csv")


#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


#creating attendance button
Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#exit button
Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()