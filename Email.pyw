import tkinter as tk
from tkinter import filedialog
import smtplib
from email.message import EmailMessage


attachments = []

window = tk.Tk()
window.title("Email Sender")
window.geometry("550x400")

window.resizable(False,False)
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)





notif = tk.Label(window, text="", font=('Calibri', 13),fg="red")
notif.place(x = 70, y = 290)



def send():
    try:
        msg = EmailMessage()
        username = "sdldiv4@gmail.com"
        password = "sdl@12345"
        to = email.get()
        subject = subjects.get()
        body = div.get()
        msg['subject'] = subject
        msg['from'] = username
        msg['to'] = to
        msg.set_content(body)

        for filename in attachments:
            filetype = filename.split('.')
            filetype = filetype[1]
            if filetype == "jpg" or filetype == "JPG" or filetype == "png" or filetype == "PNG":
                import imghdr
                with open(filename, 'rb') as f:
                    file_data = f.read()
                    image_type = imghdr.what(filename)
                msg.add_attachment(file_data, maintype='image', subtype=image_type, filename=f.name)

            else:
                with open(filename, 'rb') as f:
                    file_data = f.read()
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=f.name)

        if username == "" or password == "" or to == "" or body == "":
            notif.config(text="All fields required", fg="red")
            return
        else:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            notif.config(text="Email has been sent successfully", fg="green")
    except:
        notif.config(text="Error sending email", fg="red")


def reset():

  email.delete(0,'end')
  subjects.delete(0,'end')
  div.delete(0,'end')


def attachFile():
    filename = filedialog.askopenfilename(initialdir='D:/attendenceSheet',title='Please select a file')
    attachments.append(filename)
    notif.config(fg='green', text = 'Attached ' + str(len(attachments)) + ' files')

def exit():

    window.destroy()




message = tk.Label(
    window, text="E-MAIL SYSTEM",
    bg="cyan", fg="black", width=30,
    height=2, font=('times', 24, 'bold'))
message.place(x=1,y=5)


lbl = tk.Label(window, text="Kindly Use this Form below to get an Attendance",
               width=38, height=2, fg="black",
               bg="white", font=('times', 17, ' bold '))
lbl.place(x=12, y=80)

lbl2 = tk.Label(window, text="Enter Email:",
               width=12, height=2, fg="black",
               bg="white", font=('times', 15, ' bold '))
lbl2.place(x=15, y=150)

email = tk.Entry(window,
               width=30, bg="white",
               fg="green", font=('times', 15, ' bold '))
email.place(x=190, y=160)

lbl3 = tk.Label(window, text="Subject (optional):",
               width=15, height=2, fg="black",
               bg="white", font=('times', 15, ' bold '))
lbl3.place(x=18, y=190)

subjects = tk.Entry(window,
               width=30, bg="white",
               fg="green", font=('times', 15, ' bold '))
subjects.place(x=190, y=200)

lbl4 = tk.Label(window, text="Division:",
               width=10, height=2, fg="black",
               bg="white", font=('times', 15, ' bold '))
lbl4.place(x=10, y=230)

div = tk.Entry(window,
               width=30, bg="white",
               fg="green", font=('times', 15, ' bold '))
div.place(x=190, y=240)

send = tk.Button(window, text="SEND",
                     command= send , fg="white", bg="green",
                     width=10, height=2, activebackground="Red",
                     font=('times', 10, ' bold '))
send.place(x=80, y=330)

reset = tk.Button(window, text="RESET",
                     command= reset , fg="white", bg="green",
                     width=10, height=2, activebackground="Red",
                     font=('times', 10, ' bold '))
reset.place(x=180, y=330)

attach = tk.Button(window, text="ATTACH",
                     command= attachFile , fg="white", bg="green",
                     width=10, height=2, activebackground="Red",
                     font=('times', 10, ' bold '))
attach.place(x=280, y=330)

exit = tk.Button(window, text="EXIT",
                     command= exit , fg="white", bg="green",
                     width=10, height=2, activebackground="Red",
                     font=('times', 10, ' bold '))
exit.place(x=380, y=330)







window.mainloop()