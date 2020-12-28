from ..interfaces.ISource import ISource
from ..interfaces.ITransformer import ITransformer


class FrameDownsampler(ITransformer):

    def __init__(self, src : ISource, downsample : int=2):

        super().__init__(src)
        self.downsample = downsample

    def get_props(self):

        height,width,channel = super().get_props()


        if height % self.downsample:
            height = height // 2 + 1
        else:
            height = height // 2


        if width % self.downsample:
            width = width // 2 + 1
        else:
            width = width // 2

        return height,width,channel

    def read(self):

        frame = super().read()
        return frame[::self.downsample, ::self.downsample, :]