from typing import Union, List
import os
from random import choice
from ..bases import IManager
from ..sources import FileStream
from logging import warning, info


class VideoData:

    def __init__(self, root_dir: str, basename: str, intervals: [(int, int)] = None):

        self.basename = basename
        self.root_dir = root_dir

        if intervals:
            self.intervals = intervals
        else:
            self.intervals = []

    def __str__(self):
        return str({
            "basename": self.basename,
            "root_dir": self.root_dir,
            "intervals": self.intervals
        })

    def __repr__(self):
        return self.__str__()


class BinaryClassification(IManager):

    def __init__(self, video_dirs: Union[str, List[str]], label_paths: Union[str, List[str]]):

        self.video_dirs = self.get_iterable_or_exception(video_dirs, "video_dir")
        self.label_paths = self.get_iterable_or_exception(label_paths, "label_dir")
        self.videos: dict[str, VideoData] = self.find_videos()

        if len(self.videos) == 0:
            warning("BinaryClassification : No videos found. ")
        else:
            info(f"BinaryClassification : {len(self.videos)} found.")

        self.keys = list(self.videos.keys())
        self.calculate_intervals()

        self.stream = None
        self.frame_number = None
        self.current_filename = None

    def find_videos(self):

        videos = {}

        for video_dir in self.video_dirs:

            for root, dirs, files in os.walk(video_dir, topdown=False):

                for file in files:
                    # PI : Different video formats may be supported.
                    if file.endswith("mp4"):
                        videos[file] = VideoData(root, file)

        return videos

    @staticmethod
    def label_iter(path):

        with open(path) as fp:

            # I DO LOVE WALRUS OPERATOR !!
            while line := fp.readline():

                words = line.split()
                full_path = words[0]
                root_dir = os.path.dirname(full_path)
                basename = os.path.basename(full_path)

                intervals = []

                for i in range(len(words) - 1, 2, -2):
                    try:
                        end = int(words[i])
                        start = int(words[i - 1])

                        if start > 0 and end > 0:
                            intervals.append((start, end))

                    except ValueError:
                        continue

                yield VideoData(root_dir, basename, intervals)

    def calculate_intervals(self):

        for label_path in self.label_paths:

            for video_data in self.label_iter(label_path):

                if self.videos.get(video_data.basename, None):
                    self.videos[video_data.basename].intervals = video_data.intervals

    @staticmethod
    def get_iterable_or_exception(a: object, name):
        if type(a) == str:
            return [a]
        elif getattr(a, "__iter__"):
            return list(a)
        else:
            raise BaseException(f"{name} should be an iterable or a string.")

    def __iter__(self):
        key = choice(self.keys)
        video_data = self.videos[key]

        file_path = os.path.join(video_data.root_dir, video_data.basename)

        self.stream = FileStream(file_path)
        self.frame_number = 0
        self.current_filename = video_data.basename

        return self

    def __next__(self):

        try:
            data = self.stream.read()
            self.frame_number += 1

            prob = self.in_interval()

            return self.frame_number, data, prob
        except IOError:
            self.close_stream()
            raise StopIteration

    def close_stream(self):

        self.stream.close()
        self.stream = None
        self.frame_number = None

    def in_interval(self) -> float:

        for (start, end) in self.videos[self.current_filename].intervals:
            if self.frame_number >= start and self.frame_number < end:
                return 1.

        else:
            return 0.

    def __call__(self, episodes: int):

        for episode in range(episodes):

            for video_data in self.__iter__():
                yield (episode, video_data)
