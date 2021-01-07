from typing import Union
from ..bases import IDataset
from ..bases import Source


class LimitedRead(IDataset):

    def __init__(self, src: Union[IDataset, Source], total_frames: int):

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
