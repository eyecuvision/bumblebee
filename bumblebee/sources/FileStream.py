import cv2

from ..interfaces.ISource import ISource


class FileStream(ISource):

    def __init__(self, filepath: str):
        super().__init__()
        self.path = filepath
        self.cap = cv2.VideoCapture(self.path)

    def __del__(self):
        self.cap.release()

    def __len__(self):
        return self.get_duration()

    def get_duration(self):
        return self.cap.get(cv2.CAP_PROP_FRAME_COUNT) + 1
