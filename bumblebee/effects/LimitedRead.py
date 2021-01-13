from typing import Union
from ..sources import FileStream
from ..bases import Effect


class LimitedRead(Effect):

    def __init__(self, src: Union[FileStream, Effect], read_count: int):

        assert read_count > 0,"Read count must be bigger than 0."

        self.src = src
        self.cap = src.cap
        self.read_count = read_count

    def read(self):

        if self.read_count == 0:
            raise StopIteration()

        self.read_count -= 1

        return self.src.read()
