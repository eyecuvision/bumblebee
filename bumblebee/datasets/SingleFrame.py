from typing import Union
from ..bases.Source import Source
from ..bases.IDataset import IDataset


class SingleFrame(IDataset):

    def __init__(self, data_source : Union[Source]):

        self.src = data_source

    def __iter__(self):
        return self

    def get_props(self):
        return 1, *self.src.get_props()

    def __len__(self):
        return 1



