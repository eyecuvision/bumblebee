import torch

from typing import Union
from ..interfaces import ITransformer
from ..interfaces.ISource import ISource
from ..interfaces.IDataset import IDataset


class SingleFrame(IDataset):

    def __init__(self, data_source : Union[ISource,ITransformer]):

        self.src = data_source

    def __getitem__(self, item):
        return self.__next__()

    def __iter__(self):
        return self

    def get_props(self):
        return 1, *self.src.get_props()

    def __len__(self):
        return 1

    def __next__(self):
        return torch.from_numpy(super().__next__())


