import time
import pyautogui
#pip install pyautogui
import tkinter as tk
def screenshot():
    name=int(round(time.time() * 1000))
    name ='D:\SS_GUI\{}.png'.format(name)
    ing=pyautogui.screenshot('name.png')
    ing.show()

root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take screenshot",
    command = screenshot)
#if we are using Screenshot() it directly goes to this function it not wait for pressing directly execute function

button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text="Quit",
    command=quit)
close.pack()    
#OR close.pack(side=tk.LEFT)

root.mainloop()