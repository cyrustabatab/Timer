import tkinter
from tkinter import ttk


BGCOLOR = '#28ABB9'
GREEN = '#A8DDA8'
BUTTONBG = "#2D6187"

window = tkinter.Tk()
window.title('Timer')
window.minsize(width=400,height=400)
window['bg'] = BGCOLOR

minute_value= hour_value = second_value = 0 
font = ('Courier',40,'bold')
timer = None
started_timer = False
def start_timer():
    global started_timer
    started_timer = True
    if timer_label['text'] != 'TIMER':
        timer_label['text'] = 'TIMER'
    time = hour_value * 3600 + minute_value * 60 + second_value
    print(time)
    countdown(time)

def reset_timer():
    global started_timer
    started_timer = False
    timer_label['text'] = 'TIMER'
    time_label['text'] = f"00:00:00"
    second_scale.set(0)
    minute_scale.set(0)
    hour_scale.set(0)
    window.after_cancel(timer)


def countdown(time):
    global minute_value,hour_value,timer,started_timer
    temp_time = time
    hour_value = time // 3600
    temp_time -= 3600 * hour_value
    minute_value = temp_time // 60
    second_value = temp_time - (minute_value * 60)
    time_label['text'] = f"{hour_value:>02}:{minute_value:>02}:{second_value:>02}"
    if time > 0:
        timer = window.after(1000,countdown,time - 1)
    else:
        second_scale.set(0)
        minute_scale.set(0)
        hour_scale.set(0)
        timer_label['text'] = 'TIMES UP!!!!'
        started_timer = False
        window.lift()



timer_label = tkinter.Label(text='TIMER',fg=GREEN,bg=BGCOLOR,font=font)
timer_label.pack()



time_label = tkinter.Label(text='00:00:00',fg=GREEN,bg=BGCOLOR,font=font)
time_label.pack()


frame = tkinter.Frame(bg=BGCOLOR)
frame.pack()

start_button = tkinter.Button(frame,text='START',bg=BUTTONBG,fg=GREEN,font=font,command=start_timer)
start_button.pack(side='left',padx=5)

reset_button = tkinter.Button(frame,text="RESET",bg=BUTTONBG,fg=GREEN,font=font,command=reset_timer)
reset_button.pack(side='right',padx=5)


def hour_scale_used(value):
    if started_timer:
        return
    global hour_value
    hour_value = int(value)
    time_label['text'] = f"{hour_value:>02}:{minute_value:>02}:{second_value:>02}"

def minute_scale_used(value):
    if started_timer:
        return
    global minute_value
    minute_value = int(value)
    time_label['text'] = f"{hour_value:>02}:{minute_value:>02}:{second_value:>02}"

def second_scale_used(value):
    if started_timer:
        return 
    global second_value
    second_value = int(value)
    time_label['text'] = f"{hour_value:>02}:{minute_value:>02}:{second_value:>02}"






frame_1 = tkinter.Frame(bg=BGCOLOR)
frame_1.pack()

hour_label = tkinter.Label(frame_1,text='HOURS',fg=GREEN,bg=BGCOLOR,font=font)
hour_label.grid(row=0,column=0,padx=5)

hour_scale = tkinter.Scale(frame_1,from_=0,to=24,command=hour_scale_used,font=font,fg=GREEN,bg=BGCOLOR)
hour_scale.grid(row=0,column=1,padx=5,pady=5)

minute_scale = tkinter.Scale(frame_1,from_=0,to=59,command=minute_scale_used,font=font,fg=GREEN,bg=BGCOLOR)
minute_scale.grid(row=0,column=2,padx=5,pady=5)
minute_label = tkinter.Label(frame_1,text="MINUTES",fg=GREEN,bg=BGCOLOR,font=font)
minute_label.grid(row=0,column=3,padx=5)

frame_2 = tkinter.Frame(bg=BGCOLOR)
frame_2.pack()
seconds_label = tkinter.Label(frame_2,text="SECONDS",fg=GREEN,bg=BGCOLOR,font=font)
seconds_label.pack(side='left')
second_scale = tkinter.Scale(from_=0,to=59,font=font,fg=GREEN,bg=BGCOLOR,command=second_scale_used)
second_scale.pack()





window.mainloop()

