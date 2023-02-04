from ..lib import *

class Material:
    def __init__(self, name: str, master, *, image_size: Tuple[int, int] = (64, 64), starting_value: int = 0) -> None:
        self.name = name
        self.master = master

        self.image_size = image_size

        self.value = starting_value

        fp = f"content/img/material/{name}.png"

        self.label = Label(master, text=f"{name.title()}: {self.value}", compound="left", font=("Arial", 15, "bold"),
                           image=CTkPhotoImage(fp, size=image_size).image, corner_radius=25)

    def add_update(self, other_value: int | float) -> None:
        self.value += other_value
        self.label.configure(text=f"{self.name.title()}: {self.value}")

    def subtract_update(self, other_value: int | float) -> None:
        self.value += other_value
        self.label.configure(text=f"{self.name.title()}: {self.value}")

    def __add__(self, other: Any) -> None:
        if isinstance(other, int):
            self.add_update(other)
        elif isinstance(other, float):
            self.add_update(other)

    def __sub__(self, other: Any) -> None:
        if isinstance(other, int):
            self.subtract_update(other)
        elif isinstance(other, float):
            self.subtract_update(other)

    def create_label(self, x: float, y: float) -> None:
        self.master.add_new_widget(f"{self.name}label", self.label, x, y)
