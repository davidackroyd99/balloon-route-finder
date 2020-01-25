from square import Direction, GridSquare
from validators import validate_take_off, validate_landing

sqr = GridSquare()
sqr.vert_s = 4
sqr.hor_s = 3
assert(sqr.get_wind_speed() == 5) # test get_wind_speed

valid_take_off = GridSquare()
valid_take_off.hor_s = 3
valid_take_off.vert_s = 0
assert(validate_take_off(valid_take_off)) # test get_take_off

valid_take_off = GridSquare()
valid_take_off.hor_s = 6
valid_take_off.vert_s = 0
valid_take_off.bearing = 350
assert(validate_take_off(valid_take_off) == False) # test get_take_off
assert(valid_take_off.get_direction() == Direction.NORTH) # test get_direction

valid_take_off.vert_s = 6
valid_take_off.hor_s = 0
assert(valid_take_off.get_direction() == Direction.UP) # test get_direction for strong vertical speed