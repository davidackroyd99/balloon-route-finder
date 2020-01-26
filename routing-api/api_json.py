from flask.json import JSONEncoder
from route import Route

class BalloonJSONEncoder(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Route):
			return {
				"directions": obj.directions,
				"time": obj.time,
			}