import cv2

from ..sources import FileStream
from ..interfaces import IEffect


class GoTo(IEffect):

    def __init__(self, src: FileStream):
        self.src = src

    def __call__(self,frame_number : int,*args,**kwargs):
        self.goto(frame_number)

    def goto(self,frame_number : int):
        self.src.cap.set(cv2.CAP_PROP_POS_FRAMES,float(frame_number))
