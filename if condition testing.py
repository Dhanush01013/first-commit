import tkinter as tk
import random

root = tk.Tk()
root.title("Valentine 💖")
root.geometry("420x320")
root.configure(bg="#ffd6e7")  # light pink shade

# Canvas for heart
canvas = tk.Canvas(root, width=420, height=320, bg="#ffd6e7", highlightthickness=0)
canvas.place(x=0, y=0)

# Draw heart shape
canvas.create_polygon(
    210, 120,
    260, 80,
    320, 120,
    210, 260,
    100, 120,
    160, 80,
    fill="#ff4d88", outline=""
)

# Text
label = tk.Label(
    root,
    text=" Indhuuu 😍🥹 Will you be my Valentine? 💖",
    font=("Comic Sans MS", 18, "bold"),
    bg="#ffd6e7",
    fg="#b30059"
)
label.place(x=60, y=30)

# YES button action
def yes_clicked():
    label.config(text="Oo Myy Goshhh 😻🥳 What a surprise 😍😍😍")

# NO button run away
def move_no(event):
    x = random.randint(50, 350)
    y = random.randint(120, 300)
    no_btn.place(x=x, y=y)

# YES button
yes_btn = tk.Button(
    root,
    text="Yes ❤️",
    font=("Arial", 12, "bold"),
    bg="#ff66a3",
    fg="white",
    bd=0,
    padx=15,
    pady=5,
    command=yes_clicked
)
yes_btn.place(x=130, y=130)

# NO button
no_btn = tk.Button(
    root,
    text="No 💔",
    font=("Arial", 12),
    bg="#ffb3cc",
    bd=0
)
no_btn.place(x=220, y=180)
no_btn.bind("<Enter>", move_no)

root.mainloop()