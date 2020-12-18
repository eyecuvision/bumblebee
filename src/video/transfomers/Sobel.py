from scipy import ndimage

from src.datamodules.interfaces.ITransformer import ITransformer



class Sobel(ITransformer):


    def read(self):

        frame = super().read()
        return ndimage.sobel(frame)