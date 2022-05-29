from tkinter import *
import tkinter.font as font


def mouse_move(e):
    global mx, my

    mx = e.x
    my = e.y


def button_click(button):
    global count, turn

    if mx < 310 and my < 310 and button['text'] == "":
        if turn == 0:
            turn = 1
        else:
            turn = 0

    if count <= 8 and button['text'] == "":
        if turn == 0:
            button['text'] = "O"
            button['fg'] = "#9B0000"
        else:
            button['text'] = "X"
            button['fg'] = "#E63946"
        count += 1
        verify_win()


def click(e):
    global count

    if count == 8:
        result_label.config(text="Tie!")


def verify_win():
    global count, score_x, score_o

    for i in range(2):
        if i == 1:
            obj = "X"
        else:
            obj = "O"

        if button_1_1['text'] == obj and button_1_2['text'] == obj and button_1_3['text'] == obj or \
                button_2_1['text'] == obj and button_2_2['text'] == obj and button_2_3['text'] == obj or \
                button_3_1['text'] == obj and button_3_2['text'] == obj and button_3_3['text'] == obj or \
                button_1_1['text'] == obj and button_2_1['text'] == obj and button_3_1['text'] == obj or \
                button_1_2['text'] == obj and button_2_2['text'] == obj and button_3_2['text'] == obj or \
                button_1_3['text'] == obj and button_2_3['text'] == obj and button_3_3['text'] == obj or \
                button_1_1['text'] == obj and button_2_2['text'] == obj and button_3_3['text'] == obj or \
                button_1_3['text'] == obj and button_2_2['text'] == obj and button_3_1['text'] == obj:
            result_label.config(text="{} Win!".format(obj))
            if obj == "X":
                score_x += 1
                result_score_x.config(text=str(score_x))

            elif obj == "O":
                score_o += 1
                result_score_o.config(text=str(score_o))

            if button_1_1['text'] == obj and button_1_2['text'] == obj and button_1_3['text'] == obj:
                button_1_1['fg'] = "black"
                button_1_2['fg'] = "black"
                button_1_3['fg'] = "black"

            elif button_2_1['text'] == obj and button_2_2['text'] == obj and button_2_3['text'] == obj:
                button_2_1['fg'] = "black"
                button_2_2['fg'] = "black"
                button_2_3['fg'] = "black"

            elif button_3_1['text'] == obj and button_3_2['text'] == obj and button_3_3['text'] == obj:
                button_3_1['fg'] = "black"
                button_3_2['fg'] = "black"
                button_3_3['fg'] = "black"

            elif button_1_1['text'] == obj and button_2_1['text'] == obj and button_3_1['text'] == obj:
                button_1_1['fg'] = "black"
                button_2_1['fg'] = "black"
                button_3_1['fg'] = "black"

            elif button_1_2['text'] == obj and button_2_2['text'] == obj and button_3_2['text'] == obj:
                button_1_2['fg'] = "black"
                button_2_2['fg'] = "black"
                button_3_2['fg'] = "black"

            elif button_1_3['text'] == obj and button_2_3['text'] == obj and button_3_3['text'] == obj:
                button_1_3['fg'] = "black"
                button_2_3['fg'] = "black"
                button_3_3['fg'] = "black"

            elif button_1_1['text'] == obj and button_2_2['text'] == obj and button_3_3['text'] == obj:
                button_1_1['fg'] = "black"
                button_2_2['fg'] = "black"
                button_3_3['fg'] = "black"

            elif button_1_3['text'] == obj and button_2_2['text'] == obj and button_3_1['text'] == obj:
                button_1_3['fg'] = "black"
                button_2_2['fg'] = "black"
                button_3_1['fg'] = "black"

count = 9


def new_game():
    global count, turn

    button_1_1.config(text="")
    button_1_2.config(text="")
    button_1_3.config(text="")
    button_2_1.config(text="")
    button_2_2.config(text="")
    button_2_3.config(text="")
    button_3_1.config(text="")
    button_3_2.config(text="")
    button_3_3.config(text="")

    result_label.config(text="")

    count = 0
    turn = 0


root = Tk()
root.geometry("450x320")
root.resizable(False, False)
root.title("tic-tac-toe")

canva = Canvas(root, width=500, height=350)
canva.place(x=0, y=0)

Font = font.Font(size=50, weight="bold")

frame_table = Frame(canva, highlightbackground="#1D3557", highlightthickness=2)
frame_table.place(x=8, y=8, width=305, height=305)

button_1_1 = Button(canva, text="", bg="#A8DADC", activebackground="#457B9D", fg="#E63946", font=Font,
                    command=lambda: button_click(button_1_1))
button_1_1.place(x=10, y=10, width=100, height=100)

button_1_2 = Button(canva, text="", bg="#A8DADC", activebackground="#457B9D", fg="#E63946", font=Font,
                    command=lambda: button_click(button_1_2))
button_1_2.place(x=111, y=10, width=100, height=100)

button_1_3 = Button(canva, text="", bg="#A8DADC", activebackground="#457B9D", fg="#E63946", font=Font,
                    command=lambda: button_click(button_1_3))
button_1_3.place(x=212, y=10, width=100, height=100)

button_2_1 = Button(canva, text="", bg="#A8DADC", activebackground="#457B9D", fg="#E63946", font=Font,
                    command=lambda: button_click(button_2_1))
button_2_1.place(x=10, y=111, width=100, height=100)

button_2_2 = Button(canva, text="", bg="#A8DADC", activebackground="#457B9D", fg="#E63946", font=Font,
                    command=lambda: button_click(button_2_2))
button_2_2.place(x=111, y=111, width=100, height=100)

button_2_3 = Button(canva, text="", bg="#A8DADC", activebackground="#457B9D", fg="#E63946", font=Font,
                    command=lambda: button_click(button_2_3))
button_2_3.place(x=212, y=111, width=100, height=100)

button_3_1 = Button(canva, text="", bg="#A8DADC", activebackground="#457B9D", fg="#E63946", font=Font,
                    command=lambda: button_click(button_3_1))
button_3_1.place(x=10, y=212, width=100, height=100)

button_3_2 = Button(canva, text="", bg="#A8DADC", activebackground="#457B9D", fg="#E63946", font=Font,
                    command=lambda: button_click(button_3_2))
button_3_2.place(x=111, y=212, width=100, height=100)

button_3_3 = Button(canva, text="", bg="#A8DADC", activebackground="#457B9D", fg="#E63946", font=Font,
                    command=lambda: button_click(button_3_3))
button_3_3.place(x=212, y=212, width=100, height=100)

frame_gui = Frame(canva, bg="#1D3557", highlightbackground="black", highlightthickness=2)
frame_gui.place(x=320, y=8, width=120, height=305)

frame_score = Frame(canva, bg="#457B9D")
frame_score.place(x=330, y=80, width=99, height=220)

result_intro = Label(canva, text="Result:", bg="#457B9D", fg="white")
result_intro.place(x=330, y=80, width=99, height=20)

result_label = Label(canva, text="", bg="#457B9D", fg="white")
result_label.place(x=330, y=100, width=99, height=20)

result_score_intro = Label(canva, text="score:", bg="#457B9D", fg="white")
result_score_intro.place(x=330, y=120, width=99, height=20)

result_score_x = Label(canva, text="0", bg="#E63946", font=Font, fg="white")
result_score_x.place(x=335, y=150, width=90, height=60)

result_score_o = Label(canva, text="0", bg="#9B0000", font=Font, fg="white")
result_score_o.place(x=335, y=220, width=90, height=60)

button_play_again = Button(canva, text="Play again", bg="#A8DADC", activebackground="#457B9D", fg="black",
                           command=lambda: new_game())
button_play_again.place(x=330, y=20, width=100, height=50)


turn = 0
count = 0
score_x = 0
score_o = 0

root.bind("<Motion>", mouse_move)
root.bind("<Button-1>", click)
root.mainloop()
