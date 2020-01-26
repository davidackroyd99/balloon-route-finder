from validators import validate_take_off, validate_landing
from route import Route

def find_route(block, timeTarget):
	if(validate_take_off(block)):
		return fly(block, Route(), timeTarget)
	else:
		for sqr in block.neighbours:
			find_route(sqr, timeTarget)

def fly(block, route, timeTarget):
	t = (block.x, block.y, block.height)
	if(t in route.directions):
		return route

	route.directions.append(t)
	route.time += 2000 / (block.speed * 60)

	if len(route.directions) > 2 and block.height == 0:
		return route

	if(block.height < 500):
		for b in block.neighbours:
			if b.height > block.height:
				fly(b, route, timeTarget)

	if(route.time > (timeTarget * 0.8)):
		for b in block.neighbours:
			if b.height < block.height:
				if b.height == 0 and validate_landing(b):
					fly(b, route, timeTarget)

	if(len(block.neighbours) > 0):
		fly(block.neighbours[0], route, timeTarget)

	return route # we have not managed to land successfully so no route found!