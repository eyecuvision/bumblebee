import cv2

from ..bases.Source import Source


class FileStream(Source):

    def __init__(self, filepath: str):
        super().__init__()
        self.path = filepath
        self.cap = cv2.VideoCapture(self.path)

    def __del__(self):
        self.close()

    def __len__(self):
        return self.get_duration()

    def get_duration(self):
        return self.cap.get(cv2.CAP_PROP_FRAME_COUNT) + 1

    def close(self):
        self.cap.release()

    def __getitem__(self, item : int):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,item)