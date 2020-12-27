from unittest import TestCase
from unittest.mock import MagicMock
from ..bumblebee.effects import GoTo
from .Dummy import Dummy
from random import randint
import cv2


class TestGoTo(TestCase):

    def test_call(self):


        dummy = Dummy()
        dummy.cap = Dummy()
        dummy.cap.set = MagicMock(return_value=None)

        value = randint(0,2229)

        a = GoTo(dummy)
        a.goto(value)

        dummy.cap.set.assert_called()
        dummy.cap.set.assert_called_with(cv2.CAP_PROP_POS_FRAMES,value)



