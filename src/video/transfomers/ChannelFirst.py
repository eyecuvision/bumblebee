import numpy as np
from src.datamodules.interfaces.ITransformer import ITransformer



class ChannelFirst(ITransformer):


    def get_props(self):

        height,width,channel = self.src.get_props()
        return (channel,height,width)

    def read(self):

        frame = super().read()

        return np.transpose(frame,[2,0,1])