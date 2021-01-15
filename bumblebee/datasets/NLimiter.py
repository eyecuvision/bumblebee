from ..bases.Dataset import Dataset


class NLimiter(Dataset):

    def __init__(self, data_source, N: int):
        self.src = data_source
        self.N = N
        self.rem = N

    def __next__(self):

        if self.rem == 0:
            raise StopIteration
        else:
            if issubclass(self.src.__class__,Dataset):
                data = self.src.__next__()
            else:
                data = self.src.read()

            self.rem -= 1
            return data

    def __iter__(self):
        self.rem = self.N
        return self

    def get_props(self):
        return self.src.get_props()

    def __len__(self):
        return self.N

    def __getitem__(self, item):
        return self.__next__()

    def read(self):
        return self.__next__()