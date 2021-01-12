import numpy as np
from .Batch import Batch


class NumpyBatch(Batch):

    def __init__(self, src, batch_size=64, buffer_batch_ratio=2):
        super().__init__(src, batch_size, buffer_batch_ratio)
        self.batch = np.zeros((2 * batch_size, *self.src.get_props()))
        self._readfirstbatch()

