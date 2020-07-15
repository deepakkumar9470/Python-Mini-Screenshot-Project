# Python Screenshot using PyAutoGui
import time
import pyautogui
import tkinter as tk
def screenshot():
    name=int(round(time.time() * 1000))
    name='D:/Python_Screenshot/Sreenshot Gallery Images/{}.png'.format(name)
    image=pyautogui.screenshot(name)
    image.show()
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(
    frame,
    text='Take Screenshot',
    command=screenshot)
button.pack(side=tk.LEFT)

close=tk.Button(
    frame,
    text='Quit',
    command=quit)
close.pack(side=tk.LEFT)

root.mainloop()

