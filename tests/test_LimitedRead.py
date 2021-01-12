from unittest import TestCase
from unittest.mock import MagicMock

from bumblebee.effects import LimitedRead
from tests.Dummy import Dummy


class TestLimitedRead(TestCase):
    def test_read(self):
        end_value = 2
        dummy = Dummy()
        dummy.cap = Dummy()
        dummy.read = MagicMock()
        dummy.cap.release = MagicMock()

        with self.assertRaises(AssertionError):
            LimitedRead(dummy, -1)

        with self.assertRaises(AssertionError):
            LimitedRead(dummy, 0)

        limited_read = LimitedRead(dummy, end_value)

        limited_read.read()

        dummy.cap.release.assert_not_called()

        limited_read.read()

        dummy.cap.release.assert_not_called()

        limited_read.read()

        dummy.cap.release.assert_called()
