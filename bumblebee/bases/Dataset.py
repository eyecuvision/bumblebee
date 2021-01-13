

class Dataset:

    def __iter__(self):
        abstract

    def __len__(self):
        abstract

    def get_props(self):
        abstract

    def __next__(self):

        data = self.src.read()
        return data

    def __getitem__(self, item):
        return self.__next__()

    def read(self):
        return self.__next__()

