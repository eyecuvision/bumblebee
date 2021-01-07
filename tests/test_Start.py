from unittest import TestCase
from unittest.mock import MagicMock

import cv2

from ..bumblebee.effects import Start
from .Dummy import Dummy



class TestStart(TestCase):
    def test_read(self):

        start_value = 35
        dummy = Dummy()
        dummy.cap = Dummy()
        dummy.cap.set = MagicMock(return_value=None)
        dummy.cap.get = MagicMock(side_effect=[1,35])
        dummy.read = MagicMock()


        start  = Start(dummy,start_value)
        start.read()

        # Set should be called.
        # Get should be called.
        dummy.cap.get.assert_called()
        dummy.cap.set.assert_called_with(cv2.CAP_PROP_POS_FRAMES,start_value )


        #Set should not be called.
        #Get should be called.
        start.read()
        self.assertEqual(len(dummy.cap.get.mock_calls),2)
        self.assertEqual(len(dummy.cap.set.mock_calls),1)
