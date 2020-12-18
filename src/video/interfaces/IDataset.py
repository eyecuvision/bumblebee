

class IDataset:

    def __getitem__(self, item):
        abstract
    def __iter__(self):
        abstract

    def __len__(self):
        abstract

    def __next__(self):
        abstract


    def get_props(self):
        abstract