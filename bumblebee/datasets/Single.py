from typing import Union
from ..bases.Source import Source
from ..bases.IDataset import IDataset


class Single(IDataset):

    def __init__(self, data_source ):

        self.src = data_source

    def __iter__(self):
        return self

    def get_props(self):
        return self.src.get_props()

    def __len__(self):
        return 1



