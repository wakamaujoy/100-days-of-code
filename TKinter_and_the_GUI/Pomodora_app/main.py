from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
my_timer =None

# ---------------------------- TIMER RESET ------------------------------- # 
def cancel():
    window.after_cancel(my_timer)
    canvas.itemconfig(output_text, text=("00:00"))
    timer_label.config(text="TIMER", fg=GREEN)
    checkbox_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps +=1
    print(reps)
    # rep 1,3,5,7
    if reps % 2 !=0:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)


        # rep 2,4,6
    elif reps % 2 == 0:
        timer_label.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)
        # rep 8
    else:
        timer_label.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)


   # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if  count_sec < 10:
        count_sec = "0"+ str(count_sec)
    canvas.itemconfig(output_text, text=(f"{count_min}:{count_sec}"))

    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count -1)
    else:
        start_timer()

        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        checkbox_label.config(text=marks)












# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamadoro")
window.config(padx=100, pady=50)

canvas = Canvas(height=224, width=200)
image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image =image)
output_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", fg=RED, font=(FONT_NAME, 25,"bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="START", font=(FONT_NAME,10,"bold"), command=start_timer)
start_button.grid(column=0, row=2)

stop_button = Button(text="RESET", font=(FONT_NAME,10,"bold"), command=cancel)
stop_button.grid(column=2, row=2)

checkbox_label = Label(fg=RED)
checkbox_label.grid(column=1, row=3)






window.mainloop()