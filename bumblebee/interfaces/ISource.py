import cv2


class ISource:

    __ID__ = 1

    def __init__(self):
        self.id = ISource.__ID__
        ISource.__ID__ += 1
        self.cap = None

    def read(self):
        ret, frame = self.cap.read()

        if not ret:
            raise IOError("Stream {} :> Cannot get data from sources.")

        return frame


    def get_props(self):

        return (
            int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            3
        )

