import cv2

from ..interfaces.IDataSource import IDataSource


class WebStream(IDataSource):


    def __init__(self,url):

        self.url = url
        self.username = None
        self.password = None
        self.cap = None
        self.id = IDataSource.__ID__
        IDataSource.__ID__ +=1


    def set_credentials(self,username,password):

        self.username = username
        self.password = password
        self.url = "http://{}:{}@".format(username,password) + self.url
        return self

    def connect(self):
        self.cap = cv2.VideoCapture(self.url)







