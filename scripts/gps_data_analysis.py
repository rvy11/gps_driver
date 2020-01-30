#!/usr/bin/python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import numpy as np
import csv
import argparse

if __name__ == "__main__":
	time = []
	utm_north = []
	utm_east = []
	parser = argparse.ArgumentParser(description="Analyze GPS data")
	parser.add_argument("path", help="path to GPS data CSV file")
	args = parser.parse_args()

	with open(args.path) as csvfile:
		data = csv.DictReader(csvfile)
		for row in data:
			time.append(row['%time'])
			utm_north.append(row['field.utm_north'])
			utm_east.append(row['field.utm_east'])
	# _x = list(map(float, utm_north))
	# minx = min(_x)
	# x = [a - minx for a in _x]
	# _y = list(map(float, utm_east))
	# miny = min(_y)
	# y = [a - miny for a in _y]

	north = np.array(list(map(float, utm_north)))
	east = np.array(list(map(float, utm_east)))
	time = np.array(list(map(float, time)))

	print("north mean:", np.mean(north))
	print("north std:", np.std(north))
	print("east mean:", np.mean(east))
	print("east std:", np.std(east))

	north = north - np.min(north)
	east = east - np.min(east)
	time = time - np.min(time)
	
	# plot.hist2d(north, east)
	# plot.scatter(north, east, time)
	# plot.show()
	fig = plot.figure()
	ax = fig.add_subplot(111, projection='3d')
	# ax = fig.add_subplot(111)

	ax.scatter(north, east, time)

	ax.set_xlabel('Northing')
	ax.set_ylabel('Easting')
	ax.set_zlabel('Z Label')

	# fig.savefig('a.png')
	plot.show()

