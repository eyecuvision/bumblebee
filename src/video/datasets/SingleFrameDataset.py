


from ..interfaces.IDataSource import IDataSource
import torch

from ..interfaces.IDataset import IDataset


class SingleFrameDataset(IDataset):

    def __init__(self,data_source : IDataSource):

        self.src = data_source
        self.dims = self.src.get_props()


    def get_props(self):

        return (self.dims)

    def __getitem__(self, item):
        return self.__next__()

    def __iter__(self):
        return self


    def __len__(self):
        return 1

    def __next__(self):
        return torch.from_numpy(self.src.read())


