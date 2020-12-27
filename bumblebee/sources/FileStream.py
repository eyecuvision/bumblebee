import cv2

from ..interfaces.ISource import ISource


class FileStream(ISource):

    def __init__(self,filepath:str):

        self.path = filepath
        self.id = ISource.__ID__
        ISource.__ID__ +=1
        self.cap = cv2.VideoCapture(self.path)
        self.cap.open(0)


    def __del__(self):
        self.cap.release()


    def __len__(self):
        return self.get_duration()

    def get_duration(self):
        return self.cap.get(cv2.CAP_PROP_FRAME_COUNT) + 1