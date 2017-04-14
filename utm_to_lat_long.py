import utm

#print(utm.from_latlon(latitude=59.4326660, longitude=24.7600580))
# maakri (372943.93005591194, 6590370.1030127695, 35, 'V')

#print(utm.to_latlon(539195.77, 6590330.19, 35, 'V'))

# easting, northing, zone_number, zone_letter=None, northern=None

# 539195,77	6590330,19

#print(utm.to_latlon(547486.56, 6590598.79, 37, northern=True))



# lat 59.443685, 24.742689
'''
location : {
               "lat" : 59.44896559999999,
               "lng" : 24.6909906
            },
'''


'''import pyproj
p = pyproj.Proj(proj='utm', zone=35, ellps='GRS80')

x,y = p(59.44896559999999, 24.6909906)

print(x, y)
'''

utm.from_latlon()
