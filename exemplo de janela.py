# https://www.pythonguis.com/tutorials/create-gui-tkinter/

import tkinter as tk

root = tk.Tk()

root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

root.mainloop()