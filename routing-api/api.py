#!flask/bin/python

from flask import Flask, request, jsonify
from flask_cors import CORS
from square_repository import get_block
from route_finder import find_route
from api_json import BalloonJSONEncoder
import math
import stolen

app = Flask(__name__)
app.json_encoder = BalloonJSONEncoder
cors = CORS(app)

def convert_lat_lng(lat, lng):
	# distance = stolen.distance(lat, lng, 54.9, -2.5) * 1000
	# bearing = stolen.calculate_initial_compass_bearing((lat, lng), (54.9, -2.5))
	return (int(lat), int(lng))


def get_lat_lng(dx, dy):
	distance = math.sqrt((dx ** 2) + (dy ** 2)) / 1000
	bearing = stolen.bearing(dx, dy)
	print(bearing)
	return stolen.point_radial_distance(54.9, -2.5, bearing, distance)

@app.route('/routes')
def index():
	lat = request.args.get("lat")
	lng = request.args.get("lng")
	time = int(request.args.get("time"))
	
	block = get_block(*convert_lat_lng(lat, lng))
	route = find_route(block, time)
	if route is None:
		return jsonify([])
	route.directions = [[*get_lat_lng(c[0], c[1]), c[2]] for c in route.directions]
	return jsonify(route)

if __name__ == '__main__':
    app.run(debug=True)