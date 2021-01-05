import unittest
import robot_api


class TestAPI(unittest.TestCase):

  def test_run(self):
    tester = api.test_client(self)
    response = tester.post("/winerobots/1", data={"command": "run"})
    self.assertEquals(response.status_code, 200)

  def test_stop(self):
    tester = api.test_client(self)
    response = tester.post("/winerobots/1", data={"command": "stop"})
    self.assertEquals(responsa.status_code, 200)

  def test_bad_request(self):
    test = api.test_client(self)
    response = tester.post("/winerobots/1", data={"commnand": "unknown command"})
