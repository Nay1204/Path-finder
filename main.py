import tkinter as tk
from search import a_star
from rsc import *

def on_canvas_click(event):
    global START, GOAL

    x, y = event.x // GRID_SIZE , event.y // GRID_SIZE

    if (x,y) not in OBSTACLES:

        if START is None:
            START = (x,y)
            
            if START is not None:
                start_x, start_y = START
                canvas.create_rectangle(
                    start_x * GRID_SIZE, start_y * GRID_SIZE, (start_x + 1) * GRID_SIZE, (start_y + 1) * GRID_SIZE,
                    fill=COLOR_START, outline="black"
                )
                canvas.create_text(
                    start_x * GRID_SIZE + GRID_SIZE // 2, start_y * GRID_SIZE + GRID_SIZE // 2,
                    text="S", fill="white", font=("Helvetica", 10, "bold")
                )
                
        elif GOAL is None and (x,y) != START:
            GOAL = (x,y)

            if GOAL is not None:
                goal_x, goal_y = GOAL
                canvas.create_rectangle(
                    goal_x * GRID_SIZE, goal_y * GRID_SIZE, (goal_x + 1) * GRID_SIZE, (goal_y + 1) * GRID_SIZE,
                    fill=COLOR_GOAL, outline="black"
                )
                canvas.create_text(
                    goal_x * GRID_SIZE + GRID_SIZE // 2, goal_y * GRID_SIZE + GRID_SIZE // 2,
                    text="G", fill="white", font=("Helvetica", 10, "bold")
                )



def draw_grid(canvas):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            canvas.create_rectangle(
                x * GRID_SIZE, y * GRID_SIZE, (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE,
                fill=COLOR_EMPTY, outline="black"
            )
   
def draw_obstacles(canvas):
    for obstacle in OBSTACLES:
        x, y = obstacle
        canvas.create_rectangle(
            x * GRID_SIZE, y * GRID_SIZE, (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE,
            fill=COLOR_OBSTACLE, outline="black"
        )

def draw_path(canvas, path):
    for x, y in path:
        if (x,y) !=START and (x,y) != GOAL:
            canvas.create_rectangle(
                x * GRID_SIZE, y * GRID_SIZE, (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE,
                fill=COLOR_PATH, outline="black"
            )

def find_path():
    path = a_star(START, GOAL)
    if path:
        draw_path(canvas, path)


if __name__ == '__main__':

    root = tk.Tk()
    root.title("Shortest Path Finder")


    canvas = tk.Canvas(root, width=GRID_WIDTH * GRID_SIZE, height=GRID_HEIGHT * GRID_SIZE)
    canvas.pack()

    draw_grid(canvas)
    draw_obstacles(canvas)

    canvas.bind("<Button-1>", on_canvas_click)

    find_button = tk.Button(root, text="Find Path", command=find_path)
    find_button.pack()


    root.mainloop()