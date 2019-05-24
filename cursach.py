import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


class Model:
	def __init__(self,width,length,height):
		self.width = width
		self.length = length
		self.height = height
		self.generateInitialDiscreteSurface()
		self.show()
		
	#generate surface top boundary for earth box
	#complexity represents by 2 numbers, first number - grid complexity, second number - height differences on grid
	def generateInitialDiscreteSurface(self,complexity=[1,0]):
		self.amount = max(1,complexity[0] * max(width,length))
		self.nx = amount
		self.ny = amount
		self.x_space = np.linspace(0, width, self.nx)
		self.y_space = np.linspace(0, height, self.ny)
		
		self.z_space = np.full([self.nx,self.ny],height)
		for i in range(self.nx):
			for j in range(self.ny):
				self.z_space[i][j] = random.uniform(height-complexity[1],height+complexity[1])
		
	
	def show(self):
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		X, Y = np.meshgrid(self.x_space, self.y_space)
		surf = ax.plot_surface(X, Y, self.z_space)
		ax.set_xlim(0, width)
		ax.set_ylim(0, length)
		ax.set_zlim(0, height)
		plt.show()
		
	def detectQuad(self,x,y):
		if x > width || x < 0 || y > length || y < 0:
			return
		dx = width / self.nx
		dy = length / self.ny
		x0 = x//dx * dx
		x1 = x0 + dx
		y0 = y//dy * dy
		y1 = y0 + dy
		return np.array([[x0,y0],[x0,y1],[x1,y0],[x1,y1]])
		
	def getInterpolatedValue(self,x,y):
		quad = self.detectQuad(x,y)
	
if __name__ == "__main__":
	#init earth box for investigation
	#all calculation processes at first quarter -> box have such min and max corners (0,0,0) (width,length,height)
	#so width - xrange, length - yrange, height - zrange
	width = 10
	length = 10
	height = 10
	generateInitialDiscreteSurface(width,length,height,[2,1])
	
	