from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = '✔️'
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    label_01.config(text="Timer", font=(FONT_NAME, 26, "bold"),
                    fg=GREEN, bg=YELLOW, highlightthickness=0)
    global repeat
    repeat = 0
    screen.after_cancel(timer_count)
    canvas.itemconfig(timer_text, text="00:00")
    label_02.config(text="",
                    fg=GREEN, bg=YELLOW, highlightthickness=0)


# ---------------------------- TIMER MECHANISM ------------------------------- #
repeat = 0


def start():
    global repeat
    repeat += 1
    if repeat < 8 and repeat % 2 != 0:
        timer = WORK_MIN
        label_01.config(text="Work", font=(FONT_NAME, 26, "bold"),
                        fg=GREEN, bg=YELLOW, highlightthickness=0)
        label_02.config(text='⚒️', bg=YELLOW, highlightthickness=0)

    elif repeat < 8 and repeat % 2 == 0:
        timer = SHORT_BREAK_MIN
        label_01.config(text="Break", font=(FONT_NAME, 26, "bold"),
                        fg=PINK, bg=YELLOW, highlightthickness=0)
        label_02.config(text=check_mark,
                        fg=GREEN, bg=YELLOW, highlightthickness=0)

    elif repeat == 8:
        timer = LONG_BREAK_MIN
        label_01.config(text="Break", font=(FONT_NAME, 26, "bold"),
                        fg=RED, bg=YELLOW, highlightthickness=0)
        label_02.config(text=check_mark,
                        fg=GREEN, bg=YELLOW, highlightthickness=0)

    else:
        pass
    count_down(timer*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(time):

    minutes = time//60
    seconds = time % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time > 0:
        global timer_count
        timer_count = screen.after(1000, count_down, time-1)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.minsize(350, 350)
label_01 = Label()
label_01.config(text="Timer", font=(FONT_NAME, 26, "bold"),
                fg=GREEN, bg=YELLOW, highlightthickness=0)
label_01.grid(row=0, column=1)
label_02 = Label()
label_02.config(text="",
                fg=GREEN, bg=YELLOW, highlightthickness=0)
label_02.grid(row=3, column=1)

button_01 = Button()
button_01.config(text="Start", highlightthickness=0, command=start)
button_01.grid(row=2, column=0)
button_02 = Button()
button_02.config(text="Reset", highlightthickness=0, command=reset)
button_02.grid(row=2, column=2)

screen.config(padx=50, pady=50, bg=YELLOW)
screen.title("POMODORO")
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 120, text="00:00", font=(
    FONT_NAME, 24, "bold"), fill="white")
canvas.grid(row=1, column=1)
screen.mainloop()
