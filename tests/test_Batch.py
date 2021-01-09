from unittest import TestCase
from bumblebee.datasets import Batch
from bumblebee.effects import GoTo, CurrentFrame
from bumblebee.sources import FileStream
import os

import numpy as np


class TestBatchReading(TestCase):
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

    def find_difference(self, expected, result):

        reference = expected[1]

        for ind, row in enumerate(result):
            if np.array_equal(reference, row):
                return f"Result is slided {1 - ind} frames."

        return "Batch is completely wrong."

    def test_read(self):
        batch_size = 64

        video_path = os.path.join(self.ROOT_DIR, "videos", "bigbuckbunnypart3.mp4")

        stream = FileStream(video_path)
        stream_props = stream.get_props()

        goto = GoTo(stream)
        current_frame = CurrentFrame(stream)

        expected_batch = np.zeros((batch_size, *stream_props))

        for i in range(batch_size):
            expected_batch[i] = stream.read()

        goto(0)

        batch = Batch(stream, batch_size)

        iterator = iter(batch)

        frames = next(iterator)

        expected_shape = (batch_size, *stream_props)

        self.assertEqual(expected_shape, frames.shape)

        self.assertTrue(np.array_equal(expected_batch, frames), self.find_difference(expected_batch, frames))

        # Iterate to fill buffer 2*n
        for i in range(batch_size):
            next(iterator)

        frame_ind = current_frame()

        for i in range(batch_size-1):
            next(iterator)

        frames = next(iterator)

        goto(frame_ind)

        for i in range(batch_size):
            expected_batch[i] = stream.read()

        self.assertTrue(np.array_equal(expected_batch, frames), self.find_difference(expected_batch, frames))
