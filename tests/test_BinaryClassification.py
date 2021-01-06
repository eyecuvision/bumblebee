from unittest import TestCase
from random import seed
import os

from bumblebee.managers import BinaryClassification

seed(15122020)


class TestBinaryClassification(TestCase):

    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

    def test_single_video_no_label(self):

        labels = os.path.join(self.ROOT_DIR,"labels","no_label.txt")
        videos = os.path.join(self.ROOT_DIR,"videos","dir1")
        expected_epochs = 2


        manager = BinaryClassification(videos,labels)


        for epoch_counter,(frame_no,frame,prob) in manager(expected_epochs):

            self.assertEqual(prob,0)

        self.assertEqual(expected_epochs,epoch_counter+1)

    def test_single_video_single_label(self):
        labels = os.path.join(self.ROOT_DIR, "labels", "labels2.txt")
        videos = os.path.join(self.ROOT_DIR, "videos", "dir1")
        expected_epochs = 2

        manager = BinaryClassification(videos, labels)

        for epoch_counter, (frame_no, frame, prob) in manager(expected_epochs):

            if frame_no >= 15 and frame_no < 25 or frame_no >= 36 and frame_no < 40:
                self.assertEqual(prob,1)
            else:
                self.assertEqual(prob, 0)

        self.assertEqual(expected_epochs, epoch_counter + 1)



    def test_multi_video_multi_label(self):
        labels = [os.path.join(self.ROOT_DIR, "labels", "labels2.txt"),os.path.join(self.ROOT_DIR, "labels", "labels1.txt"),os.path.join(self.ROOT_DIR, "labels", "labels_repeated.txt")]
        videos = [os.path.join(self.ROOT_DIR, "videos", "dir1"), os.path.join(self.ROOT_DIR, "videos", "dir2"),
                  os.path.join(self.ROOT_DIR, "videos")]
        expected_epochs = 2

        manager = BinaryClassification(videos, labels)

        self.assertEqual(3, len(manager.videos))

        for epoch_counter, (frame_no, frame, prob) in manager(expected_epochs):

            if frame_no >= 15 and frame_no < 25 or frame_no >= 36 and frame_no < 40:
                self.assertEqual(prob, 1)
            else:
                self.assertEqual(prob, 0)

        self.assertEqual(expected_epochs, epoch_counter + 1)