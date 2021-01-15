from unittest import TestCase
from unittest.mock import MagicMock

from bumblebee.datasets import NLimiter
from tests.Dummy import Dummy


class TestNLimiter(TestCase):
    def test_get_props(self):
        end_value = 2
        dummy = Dummy()
        dummy.cap = Dummy()
        dummy.read = MagicMock()

        n_limiter = NLimiter(dummy,end_value)

        for i in range(end_value):
            n_limiter.read()

        with self.assertRaises(StopIteration):
            n_limiter.read()



        for ind,_ in enumerate(n_limiter):

            ...

        self.assertEqual(end_value-1,ind)
