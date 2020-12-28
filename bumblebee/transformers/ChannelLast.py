import numpy as np
from ..interfaces.ITransformer import ITransformer


class ChannelLast(ITransformer):

    def get_props(self):
        height, width, channel = self.src.get_props()
        return height, width, channel

    def read(self):
        frame = super().read()

        return np.transpose(frame, [1, 2, 0])
