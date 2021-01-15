from ..bases.Dataset import Dataset


class Single(Dataset):

    def __init__(self, data_source):
        self.src = data_source

    def __iter__(self):
        return self

    def get_props(self):
        return self.src.get_props()

    def __len__(self):
        return 1

    def __next__(self):
        data = self.src.read()
        return data

    def __getitem__(self, item):
        return self.__next__()

    def read(self):
        return self.__next__()
