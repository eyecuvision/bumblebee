from ..interfaces.ISource import ISource
import cv2

class DeviceStream(ISource):

    def __init__(self,device_id):

        self.device_id = device_id
        self.id = ISource.__ID__
        ISource.__ID__ +=1

        self.cap = cv2.VideoCapture(device_id)

