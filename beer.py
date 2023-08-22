import json
from PIL import Image, ImageTk

class Beer:
    def __init__(self, data):
        if data["empty"] == "true":
            self.name = ""
            self.style = ""
            self.abv = ""
            self.subtitle = ""
            self.desc = ""
            self.art_path = "./img/tappedout.png"
        else:
            self.name = data["name"]
            self.style = data["style"]
            self.abv = data["abv"]
            self.subtitle = self.style + " - " + self.abv + "%"
            self.desc = data["desc"]
            self.art_path = data["art"]
            
        image = Image.open(self.art_path).resize((435,500))
        self.art = ImageTk.PhotoImage(image)

    def __eq__(self, other):
        if not isinstance(other, Beer):
            return NotImplemented

        return self.name == other.name and self.style == other.style and self.abv == other.abv and self.desc == other.desc and self.art_path == other.art_path

def get_beers():
    file = open("beers.json")
    data = json.load(file)
    beers = []

    for i in data["beers"]:
        beer = Beer(i)
        beers.append(beer)

    return beers