import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
SPEED = 100
SPACE = 20

window = tk.Tk()
window.title("Snake Game 🐍")

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = [(100, 100), (80, 100), (60, 100)]
direction = "Right"


food = (random.randrange(0, WIDTH, SPACE),
        random.randrange(0, HEIGHT, SPACE))


food_id = canvas.create_oval(food[0], food[1],
                             food[0] + SPACE, food[1] + SPACE,
                             fill="red")


snake_ids = []

def draw_snake():
    global snake_ids
    for i in snake_ids:
        canvas.delete(i)
    snake_ids = []
    for x, y in snake:
        snake_ids.append(
            canvas.create_rectangle(x, y, x + SPACE, y + SPACE, fill="green")
        )

def move():
    global food, food_id

    x, y = snake[0]

    if direction == "Up":
        y -= SPACE
    elif direction == "Down":
        y += SPACE
    elif direction == "Left":
        x -= SPACE
    elif direction == "Right":
        x += SPACE

    new_head = (x, y)

    # Game over conditions
    if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake):
        canvas.create_text(WIDTH/2, HEIGHT/2,
                           text="GAME OVER",
                           fill="white",
                           font=("Arial", 24))
        return

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        food = (random.randrange(0, WIDTH, SPACE),
                random.randrange(0, HEIGHT, SPACE))
        canvas.delete(food_id)
        food_id = canvas.create_oval(food[0], food[1],
                                     food[0] + SPACE, food[1] + SPACE,
                                     fill="red")
    else:
        snake.pop()

    draw_snake()
    window.after(SPEED, move)

def change_direction(new_dir):
    global direction
    opposites = {"Up":"Down", "Down":"Up", "Left":"Right", "Right":"Left"}
    if new_dir != opposites.get(direction):
        direction = new_dir


window.bind("<Up>", lambda e: change_direction("Up"))
window.bind("<Down>", lambda e: change_direction("Down"))
window.bind("<Left>", lambda e: change_direction("Left"))
window.bind("<Right>", lambda e: change_direction("Right"))

draw_snake()
move()
window.mainloop()
