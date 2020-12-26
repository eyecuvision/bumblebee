import cv2

from ..streams.FileStream import FileStream
from ..interfaces.ITransformer import ITransformer


class GoTo(ITransformer):

    def __init__(self, src: FileStream):
        super().__init__(src)
        self.src = src



    def goto(self,frame_number : int)
        self.src.cap.set(cv2.CAP_PROP_POS_FRAMES,float(frame_number))