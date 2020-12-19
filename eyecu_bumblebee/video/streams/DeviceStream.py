from ..interfaces.IDataSource import IDataSource
import cv2

class DeviceStream(IDataSource):

    def __init__(self,device_id):

        self.device_id = device_id
        self.id = IDataSource.__ID__
        IDataSource.__ID__ +=1

        self.cap = cv2.VideoCapture(device_id)

