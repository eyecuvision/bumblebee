import os
from unittest import TestCase

from bumblebee.datasets import Single
from bumblebee.effects import GoTo
from bumblebee.sources import FileStream

import numpy as np


class TestSingleFrame(TestCase):
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

    def test_read(self):
        video_path = os.path.join(self.ROOT_DIR, "videos", "bigbuckbunnypart3.mp4")

        stream = FileStream(video_path)

        goto = GoTo(stream)

        expected_frame = stream.read()

        goto(0)
        single = Single(stream)
        result_frame = next(iter(single))

        self.assertEqual(expected_frame.shape, result_frame.shape)
        self.assertTrue(np.array_equal(expected_frame, result_frame), "First frame is not correct.")

        frame_ind = 35
        goto(frame_ind)
        expected_frame = stream.read()

        goto(frame_ind)
        single = Single(stream)
        result_frame = next(iter(single))

        self.assertEqual(expected_frame.shape, result_frame.shape)
        self.assertTrue(np.array_equal(expected_frame, result_frame), f"{frame_ind}th frame is not correct.")
