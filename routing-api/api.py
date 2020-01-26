#!flask/bin/python

from flask import Flask, request, jsonify
from flask_cors import CORS
from square_repository import get_block
from route_finder import find_route

app = Flask(__name__)
cors = CORS(app)

def convert_lat_lng(lat, lng):
	return(int(lat), int(lng))

@app.route('/routes')
def index():
	lat = request.args.get("lat")
	lng = request.args.get("lng")
	
	block = get_block(*convert_lat_lng(lat, lng))

	return jsonify([{"directions": find_route(block)}])

if __name__ == '__main__':
    app.run(debug=True)