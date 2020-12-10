import cv2
import numpy as np


class AI:

  """AI tailored for detecting people and bottles on images
  based on the YOLO algorithm"""

  def __init__(self):
    self.NeuralNetwork = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
    self.output_layers = [self.NeuralNetwork.getLayerNames()[i[0] - 1] for i in self.NeuralNetwork.getUnconnectedOutLayers()]
    self.targets = {"Person": 0, "Bottle": 39}
    self.target_heights = {"Person": 250, "Bottle": 25}
    self.confidence_level = 0.5


  def detect_object(self, target):

    """
    input
      target: "human" or "bottle"
    return 
      True if found else False
      widtn and height of the bounding box
    """

    # taking one frame of the video stream
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    camera.release()

    if frame is None:
      raise TypeError("No input was detected from the camera, frame = None")

    frame_height, frame_width, _ = frame.shape

    # preparing the frame for the Neural Network
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    self.NeuralNetwork.setInput(blob)
    output_neurons = self.NeuralNetwork.forward(self.output_layers)
    
    for neuron in output_neurons:
      for output_params in neuron:

        scores = output_params[5:]
        object_detected = np.argmax(scores)
        confidence = scores[object_detected]

        print(object_detected)

        if confidence >= self.confidence_level and object_detected == self.targets[target]:

          # parameters of the bounding box
          center_x = int(output_params[0] * frame_width)
          center_y = int(output_params[1] * frame_height)
          width = int(output_params[2] * frame_width)
          height = int(output_params[3] * frame_height)

          upper_left = (center_x - width // 2, center_y - height // 2)
          lower_right = (center_x + width // 2, center_y + height // 2)

          cv2.rectangle(frame, pt1=lower_right, pt2=upper_left, color=(0, 255, 0), thickness=2)
          cv2.putText(frame, target, upper_left, cv2.FONT_HERSHEY_SIMPLEX, 1.7, (200, 255, 255), 2, cv2.LINE_AA)

          return True, height, width, frame

    return False, None, None, None
  
  def determine_object_location(self, target):

    # looking around
    for d_angle in range(360):

      self.robot.direction += d_angle
      self.robot.direction %= 360
      found, width, height = self.detect_object(target)

      if found:
        distance = height / self.target_heights[target]
        return distance, self.robot.direction


if __name__ == "__main__":
  ai = AI() # the determine_object_location method won't work here because the robot class is not imported
  print(ai.detect_object("Person"))
