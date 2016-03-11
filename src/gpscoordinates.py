#!/usr/bin/env python2
"""This is a terminal program that finds the distance between 2 GPS coordinates
given in degrees. This implementation uses the Haversine formula. The formula
can be found at: https://en.wikipedia.org/wiki/Haversine_formula

Copyright (C) 2016  Wilmin Ceballos <source@wilmin.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import division
import math
from re import match

print ('''
###############################################################################
#              GPSCoordinates Copyright (C) 2016  Wilmin Ceballos             #
#                                                                             #
#               This program comes with ABSOLUTELY NO WARRANTY                #
#        This is free software, and you are welcome to redistribute it        #
#                   under  conditions set by the GNU GPLv3.                   #
###############################################################################
''')


def coorVerify(coor):
    """Verifies whether coordinates are valid.
    Latitude <= abs(90 degrees)
    Longitude <= abs(180 degrees)

    Args:
        coor (list): A list containing two string elements
            coor[0] = latitude in degrees
            coor[1] = longitude in degrees

    Returns:
        latitude and longitude (bool): True if coordinates are valid
    """
    latitude = False
    longitude = False
    if abs(coor[0]) <= math.radians(90):
        latitude = True
    if abs(coor[1]) <= math.radians(180):
        longitude = True
    return latitude and longitude


def coorConvert(coor):
    """Splits the string into a list of two elements: the latitude is the
    first element and the longitude is the second element. Then, the values
    are converted to 'int' type. Finally the value is converted from degrees
    to radians.

    Args:
        coor (str): Has value in format '[0-9]+\.[0-9]+,-?[0-9]+\.[0-9]+'
            example: '40.689869,-74.0449589'

    Returns:
        coor (list): Reformated. Example:
            input  --> '40.689869,-74.0449589'
            output --> [0.7101721862551726, -1.2923283273088788]
    """
    coor = coor.split(',')
    coor[0] = math.radians(eval(coor[0]))
    coor[1] = math.radians(eval(coor[1]))
    return coor


radius = 6371  # Radius of earth in kilometers
coor1 = ''
coor2 = ''

print 'Find the distance between two GPS coordinates given in degrees'
print 'With no spaces and separated by comma:'

while(True):
    coor1 = raw_input('Enter first coordinate (ex: 40.689869,-74.0449589)\n')
    if match('[0-9]+\.[0-9]+,-?[0-9]+\.[0-9]+', coor1):
        coor1 = coorConvert(coor1)
        if coorVerify(coor1):
            break
    print 'Invalid, enter the first coordinate again'

while(True):
    coor2 = raw_input('Enter second coordinate (ex: 40.689869,-74.0449589)\n')
    if(match('[0-9]+\.[0-9]+,-?[0-9]+\.[0-9]+', coor2)):
        coor2 = coorConvert(coor2)
        if coorVerify(coor2):
            break
    print 'Invalid, enter the second coordinate again'

# Haversine:
d_phi = coor2[0] - coor1[0]  # Change in latitude (lat2 - lat1)
d_lamda = coor2[1] - coor1[1]  # Change in longitude (lon2 - lon1)

a = (math.sin(d_phi/2)**2 + math.cos(coor1[0]) * math.cos(coor2[0]) *
     math.sin(d_lamda/2)**2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
distance_km = radius * c  # Distance between coordinates in kilometers
distance_mi = distance_km * 0.621371

print ('''
\nCoordinate 1: {a1},{a2}\nCoordinate 2: {b1},{b2}\n
Distance km: {km}\nDistance mi: {mi}
'''.format(a1=math.degrees(coor1[0]), a2=math.degrees(coor1[1]),
           b1=math.degrees(coor2[0]), b2=math.degrees(coor2[1]),
           km=distance_km, mi=distance_mi))
