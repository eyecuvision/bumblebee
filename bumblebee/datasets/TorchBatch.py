from bumblebee.bases import IDataset

import torch


class TorchBatch(IDataset):
    def __init__(self, src, batch_size=64, device="cpu"):
        self.src = src
        self.batch_size = batch_size
        self.batch = torch.zeros((2 * batch_size, *self.src.get_props())).to(device)
        self._head = 0
        self._readfirstbatch()

    def get_props(self):
        return self.batch_size, *self.src.get_props()

    def __iter__(self):
        return self

    def _readfirstbatch(self):
        for i in range(self.batch_size - 1):
            self.batch[i] = torch.from_numpy(super().__next__())

        self._head = self.batch_size - 1

    def __len__(self):
        return self.batch_size

    def __next__(self):
        next_frame = torch.from_numpy(super().__next__())
        self.batch[self._head] = next_frame
        self._head += 1

        if self._head == 2 * self.batch_size:
            self.batch[0:self.batch_size] = self.batch[self.batch_size:]
            self._head = self.batch_size

        return self.batch[self._head - self.batch_size:self._head]
