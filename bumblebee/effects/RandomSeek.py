from typing import Union

import cv2
from ..sources import FileStream
from ..bases import Effect
from random import randint


class RandomSeek(Effect):

    def __init__(self, src: Union[FileStream, Effect], begin_offset=0, end_offset=0):
        self.src = src
        self.cap = src.cap
        self.duration = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.begin_offset = begin_offset
        self.end_offset = end_offset
        self._distribution = randint


    def set_distribution(self,new_dist):
        self._distribution = new_dist

        result = new_dist(self.begin_offset, self.duration - 1 - self.end_offset)
        assert type(result) == int, "Expected distribution function to return integer."

        return self

    def __call__(self, *args, **kwargs):
        frame_index = self._distribution(self.begin_offset, self.duration - 1 - self.end_offset)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

        return frame_index
