from turtle import *
Tur1 = turtlemove(1000,1000)

def koch_snow_flake_production(t,length,angle):
	'''replace each of the forward movement with a new production
	F -> F+F--F+F'''
	
	t.fw(length)
	t.lt(angle)
	t.fw(length)
	t.rt(angle)
	t.fw(length)
	t.rt(angle)
	t.fw(length)
	t.fw(length)
	t.lt(angle)
	t.fw(length)
	t.lt(angle)
	t.fw(length)
	t.rt(angle)
	t.fw(length)

def koch_snow_flake(t,range,angle=90):
	'''recursively replace each of the forward in the 
	   koch triange with a new production'''
	
	if range == 0:
		koch_snow_flake_production(t,4.1,angle)
	else:
		koch_snow_flake(t,range-1,angle)
		t.lt(angle)
		koch_snow_flake(t,range-1,angle)
		t.rt(angle)
		koch_snow_flake(t,range-1,angle)
		t.rt(angle)
		koch_snow_flake(t,range-1,angle)
		koch_snow_flake(t,range-1,angle)
		t.lt(angle)
		koch_snow_flake(t,range-1,angle)
		t.lt(angle)
		koch_snow_flake(t,range-1,angle)
		t.rt(angle)
		koch_snow_flake(t,range-1,angle)
Tur1.fw(500)
Tur1.fw(-1000)
koch_snow_flake(Tur1,4)
mainloop()
