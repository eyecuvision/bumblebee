import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api

from src.datamodules.interfaces.IDataSource import IDataSource


class WindowStream(IDataSource):

    def __init__(self,region = None):


        if region:
            self.left, self.top, x2, y2 = region
            self.width = x2 - self.left + 1
            self.height = y2 - self.top + 1
        else:
            self.width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
            self.height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            self.left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            self.top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)



    def read(self):

        hwin = win32gui.GetDesktopWindow()
        hwindc = win32gui.GetWindowDC(hwin)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, self.width, self.height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (self.width, self.height), srcdc, (self.left, self.top), win32con.SRCCOPY)

        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.height, self.width, 4)

        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(hwin, hwindc)
        win32gui.DeleteObject(bmp.GetHandle())

        return cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    def get_props(self):
        return self.height,self.width,4


if __name__ == "__main__":


    stream = WindowStream([0,25,800,625])

    while True:

        image = stream.read()
        cv2.imshow("window_stream",image)
        key = cv2.waitKey(1)
        if key in [ord("q")]:
            break