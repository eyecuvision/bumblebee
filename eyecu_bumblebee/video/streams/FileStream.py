import cv2

from ..interfaces.IDataSource import IDataSource


class FileStream(IDataSource):

    def __init__(self,filepath:str):

        self.path = filepath
        self.id = IDataSource.__ID__
        IDataSource.__ID__ +=1
        self.cap = cv2.VideoCapture(self.path)


    def __del__(self):
        self.cap.release()