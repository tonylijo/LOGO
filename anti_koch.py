'''to draw the anti koch snowflake curve'''
from turtle import *
Tur1 = turtlemove(1000,1000)

def koch_snow_flake_production(t,length,angle):
	'''replace each of the forward movement with a new production
	F -> F-F++F-F'''
	
	t.fw(length)
	t.lt(angle)
	t.fw(length)
	t.rt(angle*2)
	t.fw(length)
	t.lt(angle)
	t.fw(length)

def koch_snow_flake(t,range,angle):
	'''recursively replace each of the forward in the 
	   koch triange with a new production'''
	
	if range == 0:
		koch_snow_flake_production(t,7,angle)
	else:
		koch_snow_flake(t,range-1,angle)
		t.lt(angle)
		koch_snow_flake(t,range-1,angle)
		t.rt(angle*2)
		koch_snow_flake(t,range-1,angle)
		t.lt(angle)
		koch_snow_flake(t,range-1,angle)


def koch_snowflake_full(t,range1,angle):
	'''create a full koch snowflake triangle'''
	
	for i in range(4):
		koch_snow_flake(t,range1,angle)
		t.lt(angle*2)
Tur1.fw(250)
Tur1.fw(-580)
koch_snowflake_full(Tur1,3,60)
mainloop()
