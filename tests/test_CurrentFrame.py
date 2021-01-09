from unittest import TestCase

from bumblebee.effects import GoTo, CurrentFrame
from bumblebee.sources import FileStream

import os


class TestCurrentFrame(TestCase):
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

    def test_current_frame(self):
        video_path = os.path.join(self.ROOT_DIR, "videos", "bigbuckbunnypart3.mp4")

        stream = FileStream(video_path)
        stream_props = stream.get_props()

        goto = GoTo(stream)
        current_frame = CurrentFrame(stream)

        self.assertEqual(0, next(iter(current_frame)))

        next_frame = 35
        goto(35)
        self.assertEqual(next_frame, next(iter(current_frame)))
