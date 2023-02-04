from .lib import *

from content.classes.Building import Building
from content.classes.Material import Material


class App(Tk):
    ff = "Arial" # font family

    def __init__(self) -> None:
        super().__init__()

        self.wood = None
        self.town_hall = None
        self.energy = None
        
        self.title("Empire Builders")
        self.state("zoomed")

        self.widgets = {}
        self.buildings = {}

        self.load()

    def generate_energy(self):
        while True:
            for building in self.buildings.values():
                building.generate_energy()

            sleep(1)

    def load(self) -> None:
        """Load the game"""

        self.remove_all_widgets()

        self.widgets["button01"] = (
            Button(self, corner_radius=25, fg_color="#262626", text="Play", font=(self.ff, 25, "bold"),
                   hover_color="#252525", command=self.play),
            .5, .2
        )

        self.create_all_widgets()

    def play(self) -> None:
        """The play method"""

        self.remove_all_widgets()
        
        self.energy = Material("energy", self, image_size=(32, 32))
        self.energy.create_label(.05, .05)
        
        self.wood = Material("wood", self, image_size=(32, 32))
        self.wood.create_label(.05, .1)

        self.town_hall = Building("town_hall", 1.0, self, self.buildings, size=(84, 84))
        self.town_hall.create_building(.5, .5)

        self.create_all_widgets()

        generator = Thread(target=self.generate_energy)
        generator.daemon = True
        generator.start()

    def add_new_widget(self, name: str, widget, x: float, y: float) -> None:
        """Adds a new widget"""

        self.widgets[name] = (
            widget, x, y
        )

        widget.place(relx=x, rely=y, anchor="c")

    def create_all_widgets(self) -> None:
        """Creates all the widgets in the widgets dictionary"""

        for widget in self.widgets.values():
            widget[0].place(relx=widget[1], rely=widget[2], anchor="c")

    def remove_all_widgets(self) -> None:
        """Removes all the widgets in the widgets dictionary"""

        for widget in self.widgets.values():
            widget[0].destroy()

        self.widgets = {}
