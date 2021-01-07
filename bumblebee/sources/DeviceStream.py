from ..bases.Source import Source
import cv2

class DeviceStream(Source):

    def __init__(self, device_id):

        super().__init__()
        self.device_id = device_id
        self.cap = cv2.VideoCapture(device_id)

    def close(self):
        self.cap.release()

    def __del__(self):
        self.close()