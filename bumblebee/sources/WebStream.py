import cv2

from ..bases.Source import Source


class WebStream(Source):

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.username = None
        self.password = None
        self.cap = None

    def set_credentials(self, username, password):
        self.username = username
        self.password = password
        self.url = "http://{}:{}@".format(username, password) + self.url
        return self

    def connect(self):
        self.cap = cv2.VideoCapture(self.url)
