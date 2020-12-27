from scipy import ndimage

from ..interfaces.ITransformer import ITransformer

class Sobel(ITransformer):

    def read(self):

        frame = super().read()
        return ndimage.sobel(frame)
