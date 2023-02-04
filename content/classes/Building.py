from ..lib import *

class Building:
    def __init__(self, name: str, energy_production: float, master, buildings: dict, *,
                 size: Tuple[int, int] = (20, 20)) -> None:
        self.name = name
        self.energy_production = energy_production

        self.master = master

        fp = f"content/img/building/{name}.png"

        buildings[self.name] = self

        self.label = Label(master, image=CTkPhotoImage(fp, size=size).image, text="",
                           compound="left", corner_radius=0)

    def generate_energy(self):
        self.master.energy += self.energy_production

    def create_building(self, x: float, y: float) -> None:
        self.master.add_new_widget(self.name, self.label, x, y)
