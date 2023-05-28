#!/bin/python3

print("Loading...")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio
import os
os.system("clear")
def animate_bouncing_rectangle(width, height, small_width, small_height, bounce_limit, FPS, dx, line):
    os.system("clear")
    print("Creating Plot...")
    fig, ax = plt.subplots(figsize=(width, height))
    ax.axis('off')
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    os.system("clear")
    print("Defining Variables...")
    bounce_count = 0
    duration = 100
    x = 0.0
    y = 0.0
    dy = dx
    path_x = []
    path_y = []
    os.system("clear")
    print("Defining Update Loop...")
    def update(frame):
        nonlocal x, y, dx, dy, bounce_count
        ax.cla()
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        if line:
            ax.plot(path_x, path_y, color='gray', linestyle='--')
        ax.add_patch(plt.Rectangle((x, y), small_width, small_height, color='blue'))
        x += dx
        y += dy
        if line:
            path_x.append(x+small_width/2)
            path_y.append(y+small_height/2)
        if x <= 0 or x + small_width >= width:
            dx *= -1
            bounce_count += 1
        if y <= 0 or y + small_height >= height:
            dy *= -1
            bounce_count += 1
        if bounce_count >= bounce_limit:
            anim.event_source.stop()
    os.system("clear")
    print("Creating Animation... This might take a while.")
    anim = animation.FuncAnimation(fig, update, frames=FPS, interval=5)
    os.system("clear")
    #print("Saving File... This might take a while.")
    #anim.save('bouncing_rectangle.gif', writer='pillow', fps=FPS)
    #os.system("clear")
    print("Close the GIF to exit.")
    plt.show()
print(" --- Settings --- ")
width = input("Width of simulated Screen (default = 16): ")
if width == "":
    width = 16
else:
    width = int(width)
height = input("Height of simulated Screen (default = 9): ")
if height == "":
    height = 9
else:
    height = int(height)
width_sav = input("Width of simulated Screensaver (default = 2): ")
if width_sav == "":
    width_sav = 2
else:
    width_sav = int(width_sav)
height_sav = input("Height of simulated Screensaver (default = 1): ")
if height_sav == "":
    height_sav = 1
else:
    height_sav = int(height_sav)
linee = input("Show Line? (y/n, default = n): ")
if linee == "y":
    line = True
else:
    line = False
animate_bouncing_rectangle(width, height, width_sav, height_sav, 1000, 60, 0.1, line)

# (Screen Width, Screen Height, Saver Width, Saver Height, How often to bounce, Seconds to save to GIF, Speed)

