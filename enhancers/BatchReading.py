from src.datamodules.interfaces.IDataSource import IDataSource
import torch

from src.datamodules.interfaces.IDataset import IDataset
from src.datamodules.interfaces.IEnhancer import IEnhancer


class BatchReading(IEnhancer):

    def __init__(self,src : IDataset,batch_size = 64):

        self.src = src
        self.dims = self.src.get_props()

        self.batch_size = batch_size
        self.batch = []
        self._readfirstbatch()


    def get_props(self):
        return (self.batch_size,*self.dims)

    def __getitem__(self, item):
        return self.__next__()

    def __iter__(self):
        return self


    def _readfirstbatch(self):

        for i in range(self.batch_size):
            self.batch.append(self.src.__next__())


    def __len__(self):
        return self.batch_size

    def __next__(self):
        next_frame = self.src.__next__()

        self.batch.append(next_frame)
        self.batch.pop(0)

        output = torch.zeros(self.batch_size, *self.dims)

        for i in range(self.batch_size):
            output[i] = self.batch[i]

        return output

