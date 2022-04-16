from tkinter import *

running=0
seconds=0
minutes=0
hours=0
l=0

def start():
    global running
    if(not running):
        running=1
        update()

def update():
    global hours,minutes,seconds
    seconds+=1
    if(seconds==60):
        minutes+=1
        seconds=0
    elif(minutes==60):
        hours+=1
        minutes=0
    if(hours<10):
        str_hours="0"+str(hours)
    else:
        str_hours=str(hours)
    if(minutes<10):
        str_minutes="0"+str(minutes)
    else:
        str_minutes=str(minutes)
    if(seconds<10):
        str_seconds="0"+str(seconds)
    else:
        str_seconds=str(seconds)
    l.configure(text=str_hours+":"+str_minutes+":"+str_seconds)
    global time_update
    time_update=l.after(1000,update)

def stop():
    global running
    if(running):
        running=0
        l.after_cancel(time_update)

def reset():
    global running,hours,minutes,seconds
    if(not running):
        l.config(text="00:00:00")
        hours=0
        minutes=0
        seconds=0

def main():
    global l
    window=Tk()
    window.geometry('250x100')
    window.title('stopwatch')
    l=Label(window,text="00:00:00",font=('Arial bold',20))
    l.pack()
    btn1=Button(window,text='START',height=2,width=7,command=start)
    btn1.pack(side=LEFT)
    btn2=Button(window,text='STOP',height=2,width=7,command=stop)
    btn2.pack(side=LEFT)
    btn3=Button(window,text='RESET',height=2,width=7,command=reset)
    btn3.pack(side=LEFT)
    window.mainloop()

if __name__=="__main__":
    main()