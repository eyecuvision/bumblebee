from typing import Union

import cv2

from ..sources import FileStream
from ..bases import Effect


class Start(Effect):

    def __init__(self, src: Union[FileStream, Effect], start: int):
        self.src = src
        self.cap = src.cap
        self.start = start

    def read(self):
        if self.cap.get(cv2.CAP_PROP_POS_FRAMES) < self.start:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.start)

        return self.src.read()
