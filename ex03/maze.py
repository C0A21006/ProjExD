import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    delta = { #キー：押されているキー/値：移動幅リスト[x,y]
        "Up"   :[0,-1],
        "Down" :[0,+1],
        "Left" :[-1,0],
        "Right":[+1,0],
    }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)

    if cx == 1350 and cy == 750:
        label = tk.Label(text="ゴール",
                        font=("Times New Roman", 150)
                        )
        label.place(x=500, y=300)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    label = tk.Label(root,
                text="おいす～＾＾",
                font=("Ricty Diminished", 40)
                )
    label.pack()
    
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    
    maze_bg = mm.make_maze(15,9) #1:壁/0:床
    mm.show_maze(canvas, maze_bg)

    tori = tk.PhotoImage(file="fig/4.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()