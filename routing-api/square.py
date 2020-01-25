from datetime import date 
from enum import Enum
from math import atan, degrees

class Direction(Enum):
	NORTH = 1
	EAST = 2
	WEST = 3
	SOUTH = 4
	UP = 5
	DOWN = 6

class GridSquare:
	def __init__(self):
		self.lat: str = ""
		self.lng: str = ""
		self.height: int = 0
		self.vert_s: float = 0.0
		self.hor_s: float = 0.0
		self.bearing: float = 0.0
		self.time: date

	def get_wind_speed(self) -> float:
		return ((self.vert_s ** 2) + (self.hor_s ** 2)) ** 0.5
	
	def get_direction(self) -> Direction:
		# get vertical angle of velocity
		angle = 0
		
		try:
			angle = degrees(atan(abs(self.vert_s) / self.hor_s))
		except ZeroDivisionError:
			angle = 90.0

		if(angle > 45):
			if(self.vert_s > 0):
				return Direction.UP
			else:
				return Direction.SOUTH

		if(self.bearing < 45):
			return Direction.NORTH
		elif(self.bearing < 135):
			return Direction.EAST
		elif(self.bearing < 225):
			return Direction.SOUTH
		elif(self.bearing < 315):
			return Direction.WEST
		else:
			return Direction.NORTH