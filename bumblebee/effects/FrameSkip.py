from typing import Union

import cv2

from ..sources import FileStream
from ..bases import Effect


class FrameSkip(Effect):

    def __init__(self, src: Union[FileStream, Effect], skip_count: int):
        self.src = src
        self.cap = src.cap
        self.skip_count = skip_count

    def read(self):
        current_pos = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        frame = self.src.read()

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, current_pos + self.skip_count)

        return frame
