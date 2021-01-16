from ...bases import Dataset


class Batch(Dataset):
    def __init__(self, src, batch_size=64, buffer_batch_ratio=2):
        self.batch_size = batch_size
        self.buffer_batch_ratio = buffer_batch_ratio
        self.src = src
        self._head = 0
        self.first_read_after_batch_read = None

    def get_props(self):
        return self.batch_size, *self.src.get_props()

    def __iter__(self):
        return self

    def _readfirstbatch(self):

        for i in range(self.batch_size ):
            self.batch[i] = self.read()

        self._head = self.batch_size
        self.first_read_after_batch_read = True

    def __len__(self):
        return self.batch_size

    def __next__(self):

        if self.first_read_after_batch_read:
            self.first_read_after_batch_read = False
        else:
            next_frame = self.read()
            self.batch[self._head] = next_frame
            self._head += 1

            if self._head == self.buffer_batch_ratio * self.batch_size:
                self.batch[0:self.batch_size] = self.batch[-self.batch_size:]
                self._head = self.batch_size

        return self.batch[self._head - self.batch_size:self._head]

    def reset(self):
        self._readfirstbatch()
        self.first_read_after_batch_read = False
        return self.batch[self._head - self.batch_size:self._head]

    def read(self):
        return self.src.read()
