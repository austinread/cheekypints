from beer import Beer, get_beers
from PIL import Image as pil_Image, ImageTk
from threading import Thread
from tkinter import *
from tkinter import ttk

import time

root = Tk()
root.title("Cheeky Pints")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry("1280x720")

main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky="N")

header_img = pil_Image.open("./img/wilkommen.png").resize((800,60))
header_img = ImageTk.PhotoImage(header_img)
header = Label(main_frame, text="")
header["image"] = header_img
header.grid(column = 1, row = 1)

beers_frame = ttk.Frame(main_frame, padding="0 25")
beers_frame.grid(column=1, row=2)

def update_loop():
    beers = []
    while True:
        updated_beers = get_beers()
        if updated_beers != beers:
            beers = updated_beers
            for widget in beers_frame.winfo_children():
                widget.destroy()

            for i, beer in enumerate(beers):
                art = Label(beers_frame, text="")
                art["image"] = beer.art
                art.grid(column=i+1,row=1, padx=50)

                name = Label(beers_frame, text=beer.name, font=("Arial", 25))
                name.grid(column=i+1, row=2)

                sub = Label(beers_frame, text=beer.subtitle, font=("Arial", 20))
                sub.grid(column=i+1, row=3)

                desc = Label(beers_frame, text=beer.desc, wraplength=300, font=("Arial", 15))
                desc.grid(column=i+1, row=4)
        
        time.sleep(5)

update_thread = Thread(target=update_loop)
update_thread.setDaemon(True)
update_thread.start()

root.mainloop()