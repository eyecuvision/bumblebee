from ..interfaces.ITransformer import ITransformer



class Normalization(ITransformer):


    def read(self):

        frame = super().read()
        return frame * (1/255)