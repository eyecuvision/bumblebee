import cv2
from ..streams.FileStream import FileStream
from ..interfaces.ITransformer import ITransformer
from ..interfaces.constants import READ_FAILURE


class LimitedRead(ITransformer)


    def __init__(self, src: FileStream):
        super().__init__(src)
        self.src = src
        self.limit = None

    def set_limit(self,limit):
        self.limit = limit

    def read(self):

        if self.limit and self.src.cap.get(cv2.CAP_PROP_POS_FRAMES) == self.limit:
            return READ_FAILURE

        else:
            return self.src.read()
        