from .Batch import Batch
import torch


class TorchBatch(Batch):
    def __init__(self, src, batch_size=64, device="cpu", buffer_batch_ratio=2):
        super().__init__(src, batch_size, buffer_batch_ratio)
        self.batch = torch.zeros((self.buffer_batch_ratio * batch_size, *self.src.get_props())).to(device)
        self._readfirstbatch()

    def read(self):
        return torch.from_numpy(self.src.read())
