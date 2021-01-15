from ..bases.Dataset import Dataset


class NLimiter(Dataset):

    def __init__(self, data_source, N: int):
        self.src = data_source
        self.N = N

    def __next__(self):

        if self.N == 0:
            raise StopIteration
        else:
            data = self.src.read()
            self.N -= 1
            return data

    def __iter__(self):
        return self

    def get_props(self):
        return self.src.get_props()

    def __len__(self):
        return self.N
