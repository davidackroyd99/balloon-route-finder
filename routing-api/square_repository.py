import xarray as xr
from square import Direction, GridSquare
from typing import List, Tuple
from validators import validate_flight, validate_landing, validate_take_off
import math as m

def get_square(x: int, y: int, height: float):
	square = GridSquare()
	
	h = height

	if height == 0:
		h = 5.0
	
	with xr.open_dataset('wind_direction.nc') as direction_data:
		raw_data = direction_data.sel(time="2019-09-14T10:00:00", 
			projection_y_coordinate=y, projection_x_coordinate=x)
		
		dir = raw_data.sel(height=h)["wind_from_direction"].values
		dir += 180

		if dir > 360:
			dir -= 360
		
		square.bearing = dir
		square.x = x
		square.y = y
		square.height = height

	with xr.open_dataset('wind_speed.nc') as speed_data:
		raw_data = speed_data.sel(time="2019-09-14T10:00:00",
			projection_y_coordinate=y, projection_x_coordinate=x)
		
		speed = raw_data.sel(height=h)["wind_speed"].values
		square.speed = speed
	
	return square

def get_block(x, y):
	return _get_block(x, y, 0.0, x, y, [])

def _get_block(x, y, h, startx, starty, seen) -> GridSquare:
	sqr = get_square(x, y, h)

	if not validate_flight(sqr):
		return None

	id = str(x) + str(y) + str(h)
	
	if id in seen:
		return sqr
	seen.append(id)

	distance = m.sqrt((x - startx) ** 2 + (y - starty) ** 2)

	if(distance < 10000):
		sqr.neighbours = [_get_block(c[0], c[1], c[2], startx, starty, seen) for c in get_neighbours(sqr)]
		sqr.neighbours = [s for s in sqr.neighbours if s is not None]

	return sqr

def get_neighbours(sqr: GridSquare):
	retval = []

	if sqr.get_direction() == Direction.NORTH:
		retval.append((sqr.x, sqr.y + 2000, sqr.height))
	elif sqr.get_direction() == Direction.SOUTH:
		retval.append((sqr.x, sqr.y - 2000, sqr.height))
	elif sqr.get_direction() == Direction.EAST:
		retval.append((sqr.x + 2000, sqr.y, sqr.height))
	elif sqr.get_direction() == Direction.WEST:
		retval.append((sqr.x - 2000, sqr.y, sqr.height))

	if sqr.height > 0:
		retval.append((sqr.x, sqr.y, sqr.height - 100))
	if sqr.height < 600:
		retval.append((sqr.x, sqr.y, sqr.height + 100))

	return retval

# def get_landing_zones(cube: List[List[List[GridSquare]]]) -> List[Tuple[int, int]]:
# 	retval = []

# 	for row in cube:
# 		for column in row:
# 			if validate_landing(column[0]):
# 				retval.append((column[0].x, column[0].y))
	
# 	return retval