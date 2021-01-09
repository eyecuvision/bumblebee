from typing import Union

import cv2

from ..sources import FileStream
from ..bases import IEffect


class CurrentFrame(IEffect):

    def __init__(self, src: Union[FileStream,IEffect]):
        self.src = src
        self.cap = src.cap

    def __iter__(self):
        return self

    def __next__(self):

        if self.cap.isOpened():
            return int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        else:
            raise StopIteration()
