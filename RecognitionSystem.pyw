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
    date_label['text'] = curr_day +',' +curr_date + ' '+ curr_month

clock_label = tk.Label(window,font= 'arial 33',fg = 'black')
clock_label.place(x=100,y=290)
date_label = tk.Label(window,font= 'arial 28',fg = 'black')
date_label.place(x=30,y=240)
display_time()




cap = cv2.VideoCapture(0)

def attendance():
    subprocess.run("pythonw recognizenew.pyw")

def entryToday():
    today = date.today()
    strToday = today.strftime('%y-%m-%d')

    os.startfile("D:/attendenceSheet/" + strToday)

def sentmail():
    subprocess.run("pythonw Email.pyw")

def destroy():
    if messagebox.askyesno('Quit', 'Are you sure you want to exit ? ', icon = 'question') == True:
        window.destroy()
    else:
        pass



takeImg = tk.Button(window, text="TAKE ATTENDANCE",
                    command=attendance, fg="white", bg="green",
                    width=18, height=3, activebackground="Red",
                    font=('times', 10, ' bold '))
takeImg.place(x=90, y=620)



entry = tk.Button(window, text="TODAY'S ENTRY",
                     command=entryToday, fg="white", bg="green",
                     width=14, height=3, activebackground="Red",
                     font=('times', 10, ' bold '))
entry.place(x=290, y=620)
open = tk.Button(window, text="SEND MAIL",
                     command=sentmail, fg="white", bg="green",
                     width=14, height=3, activebackground="Red",
                     font=('times', 10, ' bold '))
open.place(x=470, y=620)
quitWindow = tk.Button(window, text="QUIT",
                       command=destroy, fg="white", bg="green",
                       width=14, height=3, activebackground="Red",
                       font=('times', 10, ' bold '))
quitWindow.place(x=650, y=620)

window.mainloop()
