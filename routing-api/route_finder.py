from validators import validate_take_off

def find_route(block):
	if(validate_take_off(block)):
		return fly(block, [])
	else:
		for sqr in block.neighbours:
			find_route(sqr)

def fly(block, route):
	print((block.x, block.y, block.height))
	route.append((block.x, block.y, block.height))

	if(block.height < 500):
		for b in block.neighbours:
			if b.height > block.height:
				fly(block, route)

	if(len(block.neighbours) > 0):
		fly(block.neighbours[0], route)

	return route