import supergame
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("500x300")
img = ImageTk.PhotoImage(Image.open("supergame.gif"))  
image_label = tk.Label(image=img)
image_label.place(x=0, y=0, relwidth=1, relheight=1)
game = supergame.Supergame(root, ["производная", "первообразная"], ["Скорость изменения функции в данной точке:", "Функция, производная которой равна данной функции:"])
root.mainloop()