from tkinter import *
fen = Tk()
fen.title("Robot_world")
fen.geometry("500x500")



canvas = Canvas(fen, width=150, height=120, background='yellow')
ligne1 = canvas.create_rectangle(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()

fen.mainloop()
