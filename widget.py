from Tkinter import *
import socket

def internal_IP():
    ip = socket.gethostbyname(socket.gethostname())
    return(ip)

def switch_IP():
    return "10.228.63.20"

def switch_Port():
    return "4"

window = Tk()
window.title("IP Checker")

window.overrideredirect(True)
window.configure(background='black')

screenwidth = window.winfo_screenwidth()
windowwidth = window.winfo_width()
distance = screenwidth - windowwidth
window.geometry('+'+str(distance-250)+'+0')

window.geometry('250x80')

intlbl = Label(window, fg="white",bg="black",text="Internal IP: ", font=("Arial Bold", 14),anchor='w')
intlbl.grid(column=0, row=1)


internalResult = Label(window, bg="black",fg="white",text=internal_IP(),font=("Arial", 13))
internalResult.grid(column=1, row=1)


swlbl = Label(window, fg="white",bg="black",text="Switch IP: ", font=("Arial Bold", 14),anchor='w')
swlbl.grid(column=0, row=2)

switchResult = Label(window, fg="white",bg="black",text=switch_IP(), font=("Arial", 13))
switchResult.grid(column=1, row=2)

swplbl = Label(window, fg="white",bg="black",text="Switch Port: ", font=("Arial Bold", 14),anchor='w')
swplbl.grid(column=0, row=3)

switchPResult = Label(window, fg="white",bg="black",text=switch_Port(), font=("Arial", 13))
switchPResult.grid(column=1, row=3)

window.attributes("-transparentcolor", 'black')

window.mainloop()

window.update()
