from unittest import TestCase
from unittest.mock import MagicMock

from bumblebee.effects import End
from tests.Dummy import Dummy


class TestEnd(TestCase):
    def test_read(self):

        end_value = 35
        dummy = Dummy()
        dummy.cap = Dummy()
        dummy.cap.get = MagicMock(side_effect=[35,36])
        dummy.cap.set = MagicMock()
        dummy.read = MagicMock(side_effect = [None,None])
        dummy.cap.release = MagicMock()

        end  = End(dummy,end_value)

        end.read()
        # Get should be called.
        # Release should not be called.
        dummy.cap.get.assert_called()
        dummy.cap.release.assert_not_called()


        #Get should not be called.
        #Release should be called.
        end.read()
        dummy.cap.set.assert_called()