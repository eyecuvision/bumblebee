import cv2
from typing import Union
from ..sources import FileStream
from ..bases import Effect


class End(Effect):

    def __init__(self, src: Union[FileStream, Effect], end: int):
        self.src = src
        self.cap = src.cap
        self.end = end

    def read(self):
        if self.cap.get(cv2.CAP_PROP_POS_FRAMES) > self.end:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)

        return self.src.read()
