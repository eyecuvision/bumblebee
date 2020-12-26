import cv2

from ..streams.FileStream import FileStream
from ..interfaces.ITransformer import ITransformer


class GoTo(ITransformer):

    def __init__(self, src: FileStream):
        super().__init__(src)
        self.src = src

    def read(self,frame_number=None):

        if frame_number is not None:
            self.src.cap.set(cv2.CAP_PROP_POS_FRAMES,frame_number)

        return super().read()
