from ..interfaces.ITransformer import ITransformer

class GrayScale(ITransformer):

    def get_props(self) -> (int,int,int):

        height, width, _ = super().get_props()

        return height, width, 1


    def read(self):

        frame = super().read()
        gray_frame = .3 * frame[:,:,0] + .59 * frame[:,:,1] + .11 * frame[:,:,2]

        return gray_frame.reshape((*gray_frame.shape,1))

