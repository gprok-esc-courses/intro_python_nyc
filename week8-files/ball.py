from tkinter import Tk, Canvas

def animate():
    global dx, dy
    pos = canvas.coords(ball)
    if pos[0] <= 0 or pos[2] >= 600:
        dx = -dx 
    if pos[1] <= 0 or pos[3] >= 400:
        dy = -dy
    canvas.move(ball, dx, dy)
    window.after(30, animate)

dx = 3
dy = 2

window = Tk() 
window.title("Bouncing Ball")

canvas = Canvas(window, width=600, height=400, bg="white")
canvas.pack()

ball = canvas.create_oval(
            50, 50, 100, 100,
            fill='red',
            outline='darkblue'
        )

animate()
window.mainloop()