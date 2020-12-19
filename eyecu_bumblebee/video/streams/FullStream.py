import cv2

from ..interfaces.IDataSource import IDataSource
from ..streams.FileStream import FileStream
from ..interfaces.ITransformer import ITransformer


class FullStream(IDataSource):

    def __init__(self, src: FileStream, end_frame: int = -1,start_frame=0):
        super().__init__(src)
        self.src = src
        self.end_frame = end_frame
        self.start_frame = start_frame

    def read(self):

        if self.src.cap.get(cv2.CAP_PROP_POS_FRAMES) < self.start_frame:

            self.src.cap.set(cv2.CAP_PROP_POS_FRAMES,self.start_frame)


        if self.src.cap.get(cv2.CAP_PROP_POS_FRAMES) == self.end_frame:
            return None

        try:
            frame = self.src.cap.read()
            return frame
        except Exception:
            return None