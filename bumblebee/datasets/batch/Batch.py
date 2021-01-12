from ...bases import Dataset


class Batch(Dataset):
    def __init__(self, src, batch_size=64, buffer_batch_ratio=2):
        self.batch_size = batch_size
        self.buffer_batch_ratio = buffer_batch_ratio
        self.src = src
        self._head = 0

    def get_props(self):
        return self.batch_size, *self.src.get_props()

    def __iter__(self):
        return self

    def _readfirstbatch(self):

        for i in range(self.batch_size - 1):
            self.batch[i] = self.read()

        self._head = self.batch_size - 1

    def __len__(self):
        return self.batch_size

    def __next__(self):
        next_frame = self.read()
        self.batch[self._head] = next_frame
        self._head += 1

        if self._head == self.buffer_batch_ratio * self.batch_size:
            self.batch[0:self.batch_size] = self.batch[-self.batch_size:]
            self._head = self.batch_size

        return self.batch[self._head - self.batch_size:self._head]

    def reset(self):
        self._readfirstbatch()

    def read(self):
        return super().__next__()

