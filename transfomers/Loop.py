import cv2

from src.datamodules.streams.FileStream import FileStream
from src.datamodules.interfaces.ITransformer import ITransformer


class Loop(ITransformer):

    def __init__(self, src: FileStream, end_frame: int = -1,start_frame=0):
        super().__init__(src)
        self.src = src
        self.end_frame = end_frame
        self.start_frame = start_frame

    def read(self):

        if self.src.cap.get(cv2.CAP_PROP_POS_FRAMES) < self.start_frame:

            self.src.cap.set(cv2.CAP_PROP_POS_FRAMES,self.start_frame)


        if self.src.cap.get(cv2.CAP_PROP_POS_FRAMES) == self.end_frame:
            self.src.cap.set(cv2.CAP_PROP_POS_FRAMES,self.start_frame)


        return super().read()
