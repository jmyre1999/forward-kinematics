from vpython import *
import numpy as np

LEN_P1 = 10
LEN_P2 = 6
LEN_P3 = 6

BASE_X = 8
BASE_Y = 5
BASE_Z = 4

PHI_1 = np.pi/8
PHI_2 = np.pi/4
PHI_3 = np.pi/12


def main():
	# Initial Setup
	scene = canvas(background=vector(0,0.1,0.1))
	# Floor
	box(pos=vector(BASE_X,-0.5,BASE_Z), height=0.5, width=40, length=40, color=vector(0.6,0.5,0.5))
	# Axis
	arrow(pos=vector(BASE_X,0,BASE_Z), axis=vector(20,0,0), color=color.red, shaftwidth=0.2)
	arrow(pos=vector(BASE_X,0,BASE_Z), axis=vector(0,20,0), color=color.green, shaftwidth=0.2)
	arrow(pos=vector(BASE_X,0,BASE_Z), axis=vector(0,0,20), color=color.blue, shaftwidth=0.2)
	# Base (Part 1)
	box(pos=vector(BASE_X,2,BASE_Z), height=5, width=3, length=3, color=vector(0.5,0.5,0.5))
	# Joint 1
	sphere(pos=vector(BASE_X,BASE_Y,BASE_Z), radius=0.75)

	# Build cordinate frame matricies
	T_01 = np.array([
					[np.cos(PHI_1), np.sin(PHI_1), BASE_X], 
					[-np.sin(PHI_1), np.cos(PHI_1), BASE_Z], 
					[0, 0, 1]
					])

	T_12 = np.array([
					[np.cos(PHI_2), np.sin(PHI_2), 0], 
					[-np.sin(PHI_2), np.cos(PHI_2), LEN_P1], 
					[0,0,1]
					])

	T_23 = np.array([
					[np.cos(PHI_3), np.sin(PHI_3), 0], 
					[-np.sin(PHI_3), np.cos(PHI_3), LEN_P2], 
					[0,0,1]
					])

	T_34 = np.array([
					[np.cos(0), np.sin(0), 0], 
					[-np.sin(0), np.cos(0), LEN_P3], 
					[0,0,1]
					])

	T_02 = np.matmul(T_01, T_12)

	T_03 = np.matmul(T_02, T_23)

	T_04 = np.matmul(T_03, T_34)

	# (x,y) 2
	prev_x = BASE_X
	prev_y = BASE_Y
	x = T_02.item(0,2)
	y = T_02.item(1,2)

	# Part 2
	cylinder(pos=vector(BASE_X,BASE_Y,4), radius=0.5, axis=vector(x-prev_x,y-prev_y,0), color=vector(0.5,0.5,0.5))

	# Joint 2
	sphere(pos=vector(x,y,BASE_Z), radius=0.75)

	# (x,y) 3
	prev_x = x
	prev_y = y
	x = T_03.item(0,2)
	y = T_03.item(1,2)

	# Part 3
	cylinder(pos=vector(prev_x,prev_y,4), radius=0.5, axis=vector(x-prev_x,y-prev_y,0), color=vector(0.5,0.5,0.5))

	# Joint 3
	sphere(pos=vector(x,y,BASE_Z), radius=0.75)

	# (x,y) 4
	prev_x = x
	prev_y = y
	x = T_04.item(0,2)
	y = T_04.item(1,2)

	# Part 4
	cylinder(pos=vector(prev_x,prev_y,4), radius=0.5, axis=vector(x-prev_x,y-prev_y,0), color=vector(0.5,0.5,0.5))

	# End Effector
	sphere(pos=vector(x,y,BASE_Z), radius=0.35, color=color.black)

	return

main()