#!/usr/bin/python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import csv

if __name__ == "__main__":
	time = []
	utm_north = []
	utm_east = []
	with open("2020-01-29-12-11-25.csv") as csvfile:
		data = csv.DictReader(csvfile)
		for row in data:
			time.append(row['%time'])
			utm_north.append(row['field.utm_north'])
			utm_east.append(row['field.utm_east'])
	x = list(map(float, utm_north))
	y = list(map(float, utm_east))
	time = list(map(float, time))
	# plot.hist2d(x, y)
	# plot.scatter(x, y, time)
	# plot.show()
	fig = plot.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x, y, time)

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')

	plot.show()