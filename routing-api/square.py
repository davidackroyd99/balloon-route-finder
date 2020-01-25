from datetime import date 

class GridSquare:
	def __init__(self):
		self.lat: str
		self.lng: str
		self.height: int
		self.vert_s: float
		self.hor_s: float
		self.bearing: float
		self.time: date