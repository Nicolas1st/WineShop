import unittest
from AI import AI
import cv2
import numpy


person = cv2.imread('./test_images/person.jpg')
print(type(person))
ai = AI()


class TestAI(unittest.TestCase):
  def test_find_bottle(self):
    found, height, width, frame = ai.detect_object(person, "Person")
    self.assertTrue(found, True)
    self.assertIsInstance(type(height), int)
    self.assertIsInstance(type(width), int)
    self.assertIsInstance(type(frame), numpy.ndarray)


