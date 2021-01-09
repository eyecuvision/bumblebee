import numpy as np

from ..bases.IDataset import IDataset


class BatchReading(IDataset):

    def __init__(self, src, batch_size=64):

        self.src = src
        self.batch_size = batch_size
        self.batch = []
        self._readfirstbatch()

    def get_props(self):
        return self.batch_size, *self.src.get_props()

    def __iter__(self):
        return self

    def _readfirstbatch(self):

        for i in range(self.batch_size):
            self.batch.append(super().__next__())

    def __len__(self):
        return self.batch_size

    def __next__(self):
        next_frame = super().__next__()

        self.batch.append(next_frame)
        self.batch.pop(0)

        output = np.zeros((self.batch_size, *self.src.get_props()))

        for i in range(self.batch_size):
            output[i] = self.batch[i]

        return output
