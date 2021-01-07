from typing import Union, List
import os


class IManager:

    def __iter__(self):
        abstract

    def __next__(self):
        abstract

    def __call__(self, episodes: int):
        abstract
