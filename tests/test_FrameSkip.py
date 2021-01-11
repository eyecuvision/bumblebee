from unittest import TestCase
from unittest.mock import MagicMock

from bumblebee.effects.FrameSkip import FrameSkip
from tests.Dummy import Dummy
from cv2 import CAP_PROP_POS_FRAMES

class TestFrameSkip(TestCase):
    def test_read(self):

        skip_count = 5
        current_frame = 35

        dummy = Dummy()
        dummy.cap = Dummy()
        dummy.cap.get = MagicMock(side_effect=[current_frame])
        dummy.read = MagicMock()
        dummy.cap.set = MagicMock()

        frame_skip = FrameSkip(dummy,skip_count)

        frame_skip.read()
        dummy.cap.set.assert_called_with(CAP_PROP_POS_FRAMES,skip_count + current_frame)


