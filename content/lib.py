from customtkinter import (
    CTk as Tk,
    CTkButton as Button,
    CTkLabel as Label,
    CTkFrame as Frame,
    CTkEntry as Entry,
    CTkSlider as Slider,
    CTkImage,
    set_appearance_mode,
    set_default_color_theme
)

from pickle import load, dump
from typing import Any, Tuple

from threading import Thread
from time import sleep

from PIL import Image


class CTkPhotoImage:
    def __init__(self, file: str, *, size: Tuple[int, int] = (20, 20)) -> None:
        self.__file = file
        self.__size = size
        self.__image = Image.open(file)

    @property
    def image(self) -> CTkImage:
        return CTkImage(self.__image, size=self.__size)


class Pickler:
    @staticmethod
    def write_data(obj: Any, filename: str):
        with open(filename, "w") as fp:
            dump(obj, fp)

    @staticmethod
    def read_data(filename: str):
        with open(filename, "r") as fp:
            return load(fp)
