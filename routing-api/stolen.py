from math import asin,cos,pi,sin, atan2
import numpy as np
import numpy.linalg as la

rEarth = 6371.01 # Earth's average radius in km
epsilon = 0.000001 # threshold for floating-point equality


def deg2rad(angle):
	return angle*pi/180


def rad2deg(angle):
	return angle*180/pi

def bearing(dx, dy):
	return rad2deg(atan2(dx, dy)) + 90

def distance(s_lat, s_lng, e_lat, e_lng):

   # approximate radius of earth in km
   R = 6373.0

   s_lat = s_lat*np.pi/180.0                 
   s_lng = deg2rad(s_lng)     
   e_lat = deg2rad(e_lat)                       
   e_lng = deg2rad(e_lng)  

   d = np.sin((e_lat - s_lat)/2)**2 + np.cos(s_lat)*np.cos(e_lat) * np.sin((e_lng - s_lng)/2)**2

   return 2 * R * np.arcsin(np.sqrt(d))


def calculate_initial_compass_bearing(pointA, pointB):
	"""
	Calculates the bearing between two points.
	The formulae used is the following:
		θ = atan2(sin(Δlong).cos(lat2),
				  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
	:Parameters:
	  - `pointA: The tuple representing the latitude/longitude for the
		first point. Latitude and longitude must be in decimal degrees
	  - `pointB: The tuple representing the latitude/longitude for the
		second point. Latitude and longitude must be in decimal degrees
	:Returns:
	  The bearing in degrees
	:Returns Type:
	  float
	"""
	if (type(pointA) != tuple) or (type(pointB) != tuple):
		raise TypeError("Only tuples are supported as arguments")

	lat1 = math.radians(pointA[0])
	lat2 = math.radians(pointB[0])

	diffLong = math.radians(pointB[1] - pointA[1])

	x = math.sin(diffLong) * math.cos(lat2)
	y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
			* math.cos(lat2) * math.cos(diffLong))

	initial_bearing = math.atan2(x, y)

	# Now we have the initial bearing but math.atan2 return values
	# from -180° to + 180° which is not what we want for a compass bearing
	# The solution is to normalize the initial bearing as shown below
	initial_bearing = math.degrees(initial_bearing)
	compass_bearing = (initial_bearing + 360) % 360
	return compass_bearing

def point_radial_distance(lat1, lon1, bearing, distance):
	"""
	Return final coordinates (lat2,lon2) [in degrees] given initial coordinates
	(lat1,lon1) [in degrees] and a bearing [in degrees] and distance [in km]
	"""
	rlat1 = deg2rad(lat1)
	rlon1 = deg2rad(lon1)
	rbearing = deg2rad(bearing)
	rdistance = distance / rEarth # normalize linear distance to radian angle

	rlat = asin( sin(rlat1) * cos(rdistance) + cos(rlat1) * sin(rdistance) * cos(rbearing) )

	if cos(rlat) == 0 or abs(cos(rlat)) < epsilon: # Endpoint a pole
		rlon=rlon1
	else:
		rlon = ( (rlon1 - asin( sin(rbearing)* sin(rdistance) / cos(rlat) ) + pi ) % (2*pi) ) - pi

	lat = rad2deg(rlat)
	lon = rad2deg(rlon)
	return (lat, lon)
