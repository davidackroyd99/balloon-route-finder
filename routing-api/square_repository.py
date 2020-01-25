import xarray as xr
from square import GridSquare

def get_square_column(x, y) -> GridSquare:
	squares = [GridSquare() for _ in range(10)]

	with xr.open_dataset('wind_direction.nc') as direction_data:
		raw_data = direction_data.sel(time="2019-09-14T10:00:00", 
			projection_y_coordinate=y, projection_x_coordinate=x)
		
		dir = raw_data.sel(height=5.0)["wind_from_direction"].values
		dir += 180

		if dir > 360:
			dir -= 360
		
		squares[0].bearing = dir
		squares[0].x = x
		squares[0].y = y
		squares[0].height = 0.0

		for i in range(1, 6):
			dir = raw_data.sel(height=i * 100)["wind_from_direction"].values
			dir += 180

			if dir > 360:
				dir -= 360
			
			squares[i].bearing = dir
			squares[i].x = x
			squares[i].y = y
			squares[i].height = i * 100

	with xr.open_dataset('wind_speed.nc') as speed_data:
		raw_data = speed_data.sel(time="2019-09-14T10:00:00",
			projection_y_coordinate=y, projection_x_coordinate=x)
		
		speed = raw_data.sel(height=5.0)["wind_speed"].values
		squares[0].speed = speed

		for i in range(1, 6):
			speed = raw_data.sel(height=i * 100)["wind_speed"].values
			
			squares[i].speed = speed
	
	return squares