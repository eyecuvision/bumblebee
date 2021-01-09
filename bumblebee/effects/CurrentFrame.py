from typing import Union

import cv2

from ..sources import FileStream
from ..bases import Effect


class CurrentFrame(Effect):

    def __init__(self, src: Union[FileStream, Effect]):
        self.src = src
        self.cap = src.cap

    def __iter__(self):
        return self

    def __next__(self):

        if self.cap.isOpened():
            return int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        else:
            raise StopIteration()

    def __call__(self, *args, **kwargs):
        if self.cap.isOpened():
            return int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        else:
            raise None