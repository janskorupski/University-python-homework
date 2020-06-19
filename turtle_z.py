"""
in this assignment we were to write an animated virus simulation in turtle.
I would just like to clarify that I personally would never write such programmes in turtle nor would I simplify the physics of solid object movement 
to such algorythms, but such were the instructions of the course, so I had to follow them
"""
from turtle import *
import random
import math
import time


rozmiary = [200,300]
quarantime = 150 #czas do wyzdrowienia
first_sick = 3
population = 80
distancers = 4
steps = 1000 #liczba kolejek symulacji
size = 10 #wielkośc kulek

def main():
	show_settings()

	Dots = create(population)

	for i in range(steps):
		draw(Dots)
		statistics(Dots,i)
		Dots = simulation(Dots)
	draw(Dots)
	statistics(Dots,i)

	screen.exitonclick()


t = Turtle() #główny, do rysowania kropek
t.penup()
t.speed(0)
t.hideturtle()

t1 = Turtle() # do wypisywania statystyk
t1.penup()
t1.speed(0)
t1.hideturtle()

t2 = Turtle() # do poczatkowego wypisania zmiennych oraz ramki
t2.penup()
t2.speed(0)
t2.hideturtle()

screen = Screen()
screen.setup (width=2.5*rozmiary[0], height=2.5*rozmiary[1], startx=0, starty=0)
screen.tracer(0,0)



def norm(x): 
	return math.sqrt(x[0]**2 + x[1]**2)

sign = lambda a: (a>0) - (a<0)

def statistics(Dots,steps):
	immune = 0
	sick = 0
	vulnerable = 0
	for i in range(len(Dots)):
		if (Dots[i][4] == "red"):
			sick = sick + 1
		elif (Dots[i][4] == "green"):
			immune = immune + 1
		elif (Dots[i][4]  == "yellow"):
			vulnerable = vulnerable + 1

	t1.clear()

	t1.goto(x = rozmiary[0] - 70, y  =rozmiary[1] - 40)
	t1.write("sick: ", True, align = "left")
	t1.write(sick)

	t1.goto(x = rozmiary[0] - 70, y  =rozmiary[1] - 30)
	t1.write("immune: ", True, align = "left")
	t1.write(immune)
	 
	t1.goto(x = rozmiary[0] - 70, y  =rozmiary[1] - 20)
	t1.write("vulnerable: ", True, align = "left")
	t1.write(vulnerable)
	
	t1.goto(x = rozmiary[0] - 70, y  =rozmiary[1] - 55)
	t1.write("steps: ", True, align = "left")
	t1.write(steps)

	screen.update()

def simulation(Dots):
	for i in range(len(Dots)):
		Dots[i][0] = Dots[i][0] + sign(Dots[i][2])
		Dots[i][1] = Dots[i][1] + sign(Dots[i][3])

		#odbijanie się od ścianek:
		if (abs(Dots[i][1]) >= rozmiary[1] - Dots[i][5]/2):
			Dots[i][3] = -Dots[i][3]
		if (abs(Dots[i][0]) >= rozmiary[0] - Dots[i][5]/2):
			Dots[i][2] = -Dots[i][2]

		#liczenie czasu choroby:
		if(Dots[i][4] == "red"):
			Dots[i][6] = Dots[i][6] + 1
		if(Dots[i][6] >= quarantime):
			Dots[i][4] = "green"

	for i in range(len(Dots)):
		for j in range(i+1,len(Dots)):
			if ( norm( [Dots[i][0] - Dots[j][0],Dots[i][1] -Dots[j][1] ]) <= Dots[i][5]/2 + Dots[j][5]/2 ):
				Dots[i][2] = -Dots[i][2]
				Dots[i][3] = -Dots[i][3]
				Dots[j][2] = -Dots[j][2]
				Dots[j][3] = -Dots[j][3]
				if (Dots[i][4] == "red" and Dots[j][4] == "yellow"):
					Dots[j][4] = "red"
				if (Dots[j][4] == "red" and Dots[i][4] == "yellow"):
					Dots[i][4] = "red"
					
	return Dots

def create(n):
	# każda kropka jest postaci: [x,y,dx,dy,color,size,time of being sick ] 
	#							  0 1 2  3    4    5       	6 
	Dots = []
	for i in range(n):
		Dots.append([]) #stwórz nową kropkę
		Dots[i].append(random.randint(-rozmiary[0]+size,rozmiary[0]-size)) #nadaj losową współrzędną poziomą
		Dots[i].append(random.randint(-rozmiary[1]+size,rozmiary[1]-size)) # oraz pionową
		Dots[i].append(random.choice([-1,1]))
		Dots[i].append(random.choice([-1,1]))
		Dots[i].append("yellow")
		Dots[i].append(size)
		Dots[i].append(0)

		for j in range(i-1):
			while ( norm( [ Dots[i][0] - Dots[j][0], Dots[i][1] - Dots[j][1] ]) < Dots[i][5] + Dots[j][5] ):
				Dots[i][0] = random.randint(-rozmiary[0]+size,rozmiary[0]-size) #nadaj losową współrzędną poziomą
				Dots[i][1] = random.randint(-rozmiary[1]+size,rozmiary[1]-size) # oraz pionową

	for dist in random.sample(Dots,distancers):
		dist[2] = 0
		dist[3] = 0

	for sick in random.sample(Dots,first_sick):
		sick[4] = "red"
	return Dots


def draw(Dots): #po otrzymaniu układu kropek, rysuje cały obraz w danym momencie

	t.clear()
	for dot in Dots:
		t.goto(x=dot[0],y=dot[1])
		t.pendown()
		t.dot(dot[5],dot[4])
		t.penup()

	screen.update()

def show_settings():

	t2.goto(x=-rozmiary[0],y = -rozmiary[1])
	t2.pendown()
	t2.goto(x=-rozmiary[0],y = rozmiary[1])
	t2.goto(x=rozmiary[0],y = rozmiary[1])
	t2.goto(x=rozmiary[0],y = -rozmiary[1])
	t2.goto(x=-rozmiary[0],y = -rozmiary[1])
	t2.penup()

	t2.goto(x = -rozmiary[0] + 5, y  =rozmiary[1] + 40)
	t2.write("czas chorowania: ", True, align = "left")
	t2.write(quarantime)

	t2.goto(x = -rozmiary[0] + 5, y  =rozmiary[1] + 30)
	t2.write("początkowa liczba osób: ", True, align = "left")
	t2.write(population)

	t2.goto(x = -rozmiary[0] + 5, y  =rozmiary[1] + 20)
	t2.write("początkowa liczba zakażonych: ", True, align = "left")
	t2.write(first_sick)

	t2.goto(x = -rozmiary[0] +180, y  =rozmiary[1] + 40)
	t2.write("liczba osób dystansujących się: ", True, align = "left")
	t2.write(distancers)

	t2.goto(x =-rozmiary[0] + 180, y  =rozmiary[1] + 30)
	t2.write("liczba kolejek symulacji: ", True, align = "left")
	t2.write(steps)

	t2.goto(x = -rozmiary[0] +180, y  =rozmiary[1] + 20)
	t2.write("wielkość kulek: ", True, align = "left")
	t2.write(size)

	screen.update()


main()

