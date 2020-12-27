from typing import Union
from ..interfaces import ITransformer
from ..interfaces.ISource import ISource
from ..interfaces.IDataset import IDataset
import torch


class VideoDataset(IDataset):

    def __init__(self, data_source: Union[ISource, ITransformer], n_frames=8):

        self.src = data_source

        self.n_frames = n_frames
        self.frames = []
        self._readfirstbatch()

    def get_props(self):

        return self.n_frames, *self.src.get_props()

    def __getitem__(self, item):
        return self.__next__()

    def __iter__(self):
        return self

    def _readfirstbatch(self):

        for i in range(self.n_frames):
            self.frames.append(self.src.read())

    def __len__(self):
        return 1

    def __next__(self):
        next_frame = super().__next__()
        self.frames.append(next_frame)
        self.frames.pop(0)

        output = torch.zeros(self.n_frames, *self.src.get_props())

        for i in range(self.n_frames):
            output[i] = torch.from_numpy(self.frames[i])

        return output
