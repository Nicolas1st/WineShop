from math import sin, cos
from AI import AI
from Manipulator import Manipulator
import cv2


class Robot:

  def __init__(self, x, y, direction):
    self.x = x
    self.y = y
    self.positions = [[x, y, direction]]
    self.AI = AI()
    self.tool = Manipulator()
    self.direction = direction


  def rotate(angle=None, direction=None):
    if angle is not None:
      self.direction += angle
    elif direciton is not None:
      self.direction = direction
    self.direction %= 360


  def move(distance):
    # always moves in the direction of self.direction
    self.x += distance * cos(self.direction)
    self.y += distance * sin(self.direction)
    self.positions.append([self.x, self.y, direction])


  def move_back(self):
    self.x = self.positions[-1][0]
    self.y = self.positions[-1][1]
    self.direciton = self.positions[-1][2]


  def use_tool():
    pass


  def determine_object_location(self, target):
    """
    input
      target: "Person", "Bottle"
    return
      distance, direction
    """

    # looking around
    for d_angle in range(360):

      self.direction += d_angle
      self.direction %= 360
      found, width, height, frame = self.AI.detect_object(target)

      if found:
        distance = height / self.AI.target_heights[target]
        cv2.imshow(target, frame)
        return distance, self.direction

  
  def deliver_object(self):
    bottle_distance, bottle_direction = self.determine_object_location("Bottle")
    human_distance, human_direction = self.determine_object_location("Person")

    self.rotate(direction=bottle_direction)
    self.move(bottle_distance)
    self.use_tool()
    
    self.move_back()

    self.rotate(direction=human_direction)
    self.move()
    self.use_tool()





if __name__ == "__main__":
  robot = Robot(0, 0, 0)
  robot.determine_object_location("Person")
