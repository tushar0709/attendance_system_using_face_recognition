import tkinter as tk
from tkinter import messagebox
import cv2
import time as tm
import os
import os.path
from PIL import Image, ImageTk
from datetime import date
import subprocess




window = tk.Tk()
window.title("Face_Recogniser")
window.geometry("858x720")

window.resizable(False,False)
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
message = tk.Label(
    window, text="Attendance System using Face Recognition",
    bg="green", fg="white", width=35,
    height=2, font=('times', 30, 'bold'))
message.place(x=5,y=20)

photo1 = ImageTk.PhotoImage(Image.open('demologo.png'))
lab = tk.Label(image= photo1)
lab.place(x=330,y=120)

photo = ImageTk.PhotoImage(Image.open('face_recg.png'))
lab = tk.Label(image= photo)
lab.place(x=210,y=240)

def display_time():

    curr_day = tm.strftime("%A")
    curr_date = tm.strftime("%d")
    curr_month = tm.strftime("%B")
    curr_time = tm.strftime("%I:%M:%S %p")
    clock_label['text'] = curr_time
    clock_label.after(200,display_time)
    date_label['text'] = curr_day +', ' +curr_date + ' '+ curr_month

clock_label = tk.Label(window,font= 'arial 33',fg = 'black')
clock_label.place(x=100,y=280)
date_label = tk.Label(window,font= 'arial 28',fg = 'black')
date_label.place(x=30,y=230)
display_time()


# lbl = tk.Label(window, text="No.",
#                width=20, height=2, fg="green",
#                bg="white", font=('times', 15, ' bold '))
# lbl.place(x=400, y=200)
#
# txt = tk.Entry(window,
#                width=20, bg="white",
#                fg="green", font=('times', 15, ' bold '))
# txt.place(x=700, y=215)
#
# lbl2 = tk.Label(window, text="Name",
#                 width=20, fg="green", bg="white",
#                 height=2, font=('times', 15, ' bold '))
# lbl2.place(x=400, y=300)
#
# txt2 = tk.Entry(window, width=20,
#                 bg="white", fg="green",
#                 font=('times', 15, ' bold '))
# txt2.place(x=700, y=315)


cap = cv2.VideoCapture(0)

def attendance():
    os.system("python bug.py")


"""def entryToday():
    today = date.today()
    strToday = today.strftime('%y-%m-%d')

    os.startfile("C:/Users/DELL/PycharmProjects/Mini_project_SDL-copy/Mini_project_SDL/attendance_sheet/" + strToday + ".csv")
"""
def sentmail():
    os.system("python GUImail.py")


def current_session():
    today = date.today()
    strToday = today.strftime('%y-%m-%d')
    session = "unknown.csv"

    now = datetime.now()
    hour = now.strftime('%H:%M')

    if hour >= '9' and hour <= '11':
        session = "session_1.csv"
        os.startfile("C:/Users/DELL/PycharmProjects/Mini_project_SDL-copy/Mini_project_SDL/session/" + strToday+"/"+ session)

    elif hour >= '11:15' and hour <= '12:15':
        session = "session_2.csv"
        os.startfile("C:/Users/DELL/PycharmProjects/Mini_project_SDL-copy/Mini_project_SDL/session/" + strToday+"/"+ session)

    elif hour >= '13:15' and hour <= '15:15':
        session = "session_3.csv"
        os.startfile("C:/Users/DELL/PycharmProjects/Mini_project_SDL-copy/Mini_project_SDL/session/" + strToday+"/"+ session)

    # print(session1, session2, session3)
def destroy():
    if messagebox.askyesno('Quit', 'Are you sure you want to exit ? ', icon = 'question') == True:
        window.destroy()
    else:
        pass

takeImg = tk.Button(window, text="TAKE ATTENDANCE",
                    command=attendance, fg="white", bg="green",
                    width=18, height=3, activebackground="Red",
                    font=('times', 10, ' bold '))
takeImg.place(x=100, y=610)



entry = tk.Button(window, text="TODAY'S ENTRY",
                     command=current_session, fg="white", bg="green",
                     width=14, height=3, activebackground="Red",
                     font=('times', 10, ' bold '))
entry.place(x=280, y=610)
open = tk.Button(window, text="SEND MAIL",
                     command=sentmail, fg="white", bg="green",
                     width=14, height=3, activebackground="Red",
                     font=('times', 10, ' bold '))
open.place(x=460, y=610)
quitWindow = tk.Button(window, text="QUIT",
                       command=destroy, fg="white", bg="green",
                       width=14, height=3, activebackground="Red",
                       font=('times', 10, ' bold '))
quitWindow.place(x=640, y=610)

window.mainloop()
