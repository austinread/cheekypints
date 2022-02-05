from beer import Beer, get_beers
from PIL import Image as pil_Image, ImageTk
from threading import Thread
from tkinter import *
from tkinter import ttk

import time

bg_color="#333333"
text_color="#EEEEEE"
font = "Helvetica"

root = Tk()
root.title("Cheeky Pints")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.configure(background=bg_color)
root.geometry("1280x720")

main_frame = Frame(root, background=bg_color)
main_frame.grid(column=0, row=0, sticky="N")

header_img = pil_Image.open("./img/wilkommen.png").resize((1000,75))
header_img = ImageTk.PhotoImage(header_img)
header = Label(main_frame, text="", background=bg_color)
header["image"] = header_img
header.grid(column = 1, row = 1, pady=(25, 0))

beers_frame = Frame(main_frame, bg=bg_color)
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
                art = Label(beers_frame, text="", border="5", background=bg_color)
                art["image"] = beer.art
                art.grid(column=i+1,row=1, padx=100, pady=(25, 0))

                name = Label(beers_frame, text=beer.name, wraplength=400, font=(font, 25), background=bg_color, fg=text_color)
                name.grid(column=i+1, row=2)

                sub = Label(beers_frame, text=beer.subtitle, wraplength=400, font=(font, 20), background=bg_color, fg=text_color)
                sub.grid(column=i+1, row=3)

                desc = Label(beers_frame, text=beer.desc, wraplength=300, font=(font, 15), background=bg_color, fg=text_color)
                desc.grid(column=i+1, row=4)
        
        time.sleep(5)

update_thread = Thread(target=update_loop)
update_thread.setDaemon(True)
update_thread.start()

root.mainloop()