from square import Direction, GridSquare
from validators import validate_take_off, validate_landing
from square_repository import get_square_column
import math as m

assert(m.isclose(get_square_column(0,0)[0].bearing, 28.8797, abs_tol=0.001))
assert(m.isclose(get_square_column(0,0)[0].speed, 5.0027866, abs_tol=0.001))