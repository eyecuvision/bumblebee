from typing import Union

import cv2
from ..sources import FileStream
from ..bases import Effect
from random import randint

class RandomSeek(Effect):

    def __init__(self, src: Union[FileStream, Effect],begin_offset = 0,end_offset = 0):
        self.src = src
        self.cap = src.cap
        self.duration = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.begin_offset = begin_offset
        self.end_offset = end_offset

    def __call__(self,frame_number : int,*args,**kwargs):
        frame_index = randint(self.begin_offset,self.duration-1 - self.end_offset)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)



