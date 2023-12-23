from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 10")

def logout():
    os.system("shutdown -1")    

def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("Shutdown App")
st.geometry("575x250")
st.config(bg="white")

r_button = Button(st,text="Restart", font=("Time New Roman",12,"bold"), relief=RAISED, cursor="plus",command=restart)
r_button.place(x=50,y=100,height=40,width=100)

rt_button = Button(st,text="Restart Time", font=("Time New Roman",11,"bold"), relief=RAISED, cursor="plus",command=restart_time)
rt_button.place(x=175,y=100,height=40,width=100)

lg_button = Button(st,text="Log Off", font=("Time New Roman",12,"bold"), relief=RAISED, cursor="plus",command=logout)
lg_button.place(x=300,y=100,height=40,width=100)

sht_button = Button(st,text="Shut Down", font=("Time New Roman",12,"bold"), relief=RAISED, cursor="plus",command=shutdown)
sht_button.place(x=425,y=100,height=40,width=100)

st.mainloop()