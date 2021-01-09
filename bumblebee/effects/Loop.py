from typing import Union

import cv2
from ..bases import Effect
from ..sources import FileStream


class Loop(Effect):

    def __init__(self, src: Union[FileStream, Effect], end_frame: int = -1, start_frame=0):
        self.src = src
        self.end_frame = end_frame
        self.start_frame = start_frame

    def read(self):

        if self.src.cap.get(cv2.CAP_PROP_POS_FRAMES) < self.start_frame:
            self.src.cap.set(cv2.CAP_PROP_POS_FRAMES, self.start_frame)

        if self.src.cap.get(cv2.CAP_PROP_POS_FRAMES) == self.end_frame:
            self.src.cap.set(cv2.CAP_PROP_POS_FRAMES, self.start_frame)

        return self.src.read()
