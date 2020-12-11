from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from robot import deliverWine.deliver_wine
import multiprocessing


app = Flask(__name__)
api = Api(app)


working_robots = {}

class RobotAPI(Resource):

  def post(self, robot_id):
    
    if request.form["commnand"] == "run":
      if robot_id not in working_robots:
        robot_thread = multiprocessing.Process(target=deliver_wine)
        robot_thread.start()
        working_robots[robot_id] = robot_thread
        return {"result": "Robot had started working"}
      else:
        return {"result": "The robot is already working"}

    elif request.form["command"] == "stop":
      if robot_id in working_robots:
        working_robots[robot_id].terminate()
        del working_robots[robot_id]
        return {"result": "The robot has been stopped"}
      else:
        return {"The robot was not working"}
      
    abort(400, message="Unknown command. Acceptable arguments for command 'run' / 'stop'")


api.add_resource(RobotAPI, "/winerobots/robot<int:robot_id>")
if __name__ == "__main__":
  app.run(debug=True)
