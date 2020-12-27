from typing import Union
from ..interfaces import IDataset
from ..interfaces import ISource
from ..interfaces import ITransformer


class LimitedRead(IDataset):

    def __init__(self, src: Union[IDataset, ISource, ITransformer], total_frames: int):

        self.src = src
        self.remaining_frames = total_frames

    def get_props(self):
        return self.src.get_props()

    def __iter__(self):
        return self

    def __len__(self):
        return 1

    def __next__(self):

        if self.remaining_frames == 0:
            raise StopIteration()
        else:
            self.remaining_frames -= 1
            return super().__next__()
