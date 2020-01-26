from square import Direction, GridSquare
from validators import validate_take_off, validate_landing
from square_repository import get_block
from route_finder import find_route
import math as m

block = get_block(100000, -20000)

print(find_route(block))