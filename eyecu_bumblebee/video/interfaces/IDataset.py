

class IDataset:

    def __getitem__(self, item):
        abstract
    def __iter__(self):
        abstract

    def __len__(self):
        abstract

    def __next__(self):

        try:
            data = self.src.read()
        except Exception:
            return data


    def get_props(self):
        return self.src.get_props()