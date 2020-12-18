from ..interfaces.IDataSource import IDataSource


class ITransformer(IDataSource):


    def __init__(self,src):

        self.src = src

    def get_props(self):
        return self.src.get_props()

    def read(self):
        return self.src.read()




