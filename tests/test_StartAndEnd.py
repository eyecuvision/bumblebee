from unittest import TestCase
from unittest.mock import MagicMock

from bumblebee.effects import End, Start
from tests.Dummy import Dummy


class TestStartAndEnd(TestCase):
    def test_read(self):

        start_frame = 35
        end_frame = start_frame + 1

        stream = Dummy()
        stream.cap = Dummy()
        stream.cap.get = MagicMock(
            side_effect=[0, 0, start_frame, start_frame , start_frame + 1, start_frame + 1,start_frame+2,start_frame+2])
        stream.cap.set = MagicMock()
        stream.cap.release = MagicMock()
        stream.read = MagicMock()

        stream = Start(stream, start_frame)
        stream = End(stream, end_frame)

        # Get is called 2 times.
        # Set is called 1 time.
        stream.read()
        self.assertEqual(len(stream.cap.get.mock_calls), 2)
        stream.cap.set.assert_called_once()
        stream.cap.release.assert_not_called()

        # Get is called 2 + 2 = 5 times.
        # Set is still called 1 time.
        stream.read()
        self.assertEqual(len(stream.cap.get.mock_calls), 4)
        stream.cap.set.assert_called_once()
        stream.cap.release.assert_not_called()


        # Get is called 2 + 2 + 2 = 6 times.
        # Set is still called 1 time.
        # Release is called 1 time.
        stream.read()
        self.assertEqual(len(stream.cap.get.mock_calls), 6)
        stream.cap.set.assert_called_once()
        stream.cap.release.assert_not_called()

        stream.read()
        self.assertEqual(len(stream.cap.get.mock_calls), 8)
        stream.cap.release.assert_called_once()
        stream.cap.set.assert_called_once()