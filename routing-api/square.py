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
		self.x: str = ""
		self.y: str = ""
		self.height: int = 0
		self.speed: float = 0.0
		self.bearing: float = 0.0
		self.time: date

	def get_direction(self) -> Direction:
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