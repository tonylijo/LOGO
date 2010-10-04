''' turtle graphics primitives
fw -> to move forward
bw -> to move backward
lt -> to turn left by an angle
rt -> to turn right by an angle'''
from Tkinter import *
import math
root_window = Tk()
class turtlemove:
	def __init__(self,widt_h=500,heigh_t=500):
		self.canvas = Canvas(root_window,width=widt_h,height=heigh_t)
		self.canvas.pack()
		self.centerx = (widt_h/2)
		self.centery = (heigh_t/2)
		self.angle = 0
	def fw(self,forward):
		startx = self.centerx
		starty = self.centery
		endx = self.centerx + (math.cos((math.pi*self.angle)/180)*forward)
		endy = self.centery + (math.sin((math.pi*self.angle)/180)*forward)
		w = self.canvas.create_line(startx,starty,endx,endy)
		self.centerx = endx
		self.centery = endy
	def bw(self,backward):
		self.fw(-backward)
	def rt(self,angle):
		self.angle = self.angle + angle
	def lt(self,angle):
		self.rt(-1*angle)
