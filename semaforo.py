from os import system, name 
from time import sleep
import random

# define our clear function https://www.geeksforgeeks.org/clear-screen-python/
def clear(): 
	# for windows 
	if name == 'nt': 
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 

def carriltr(ca, cv, c2, cdd, ce, cf, cg, ch):
	if ca == 1 :
		print("A ")
	if cv == 1 :
		print("B ")
	if c2 == 1 :
		print("C ")
	if cdd == 1 :
		print("D ")
	if ce == 1 :
		print("E ")
	if cf == 1 :
		print("F ")
	if cg == 1 :
		print("G ")
	if ch == 1 :
		print("H ")
	return

def carriltr2(ca,cv,c2,cdd,ce,cf,cg,ch):
	if ca == 0 :
		print("A ")
	if cv == 0 :
		print("B ")
	if c2 == 0 :
		print("C ")
	if cdd == 0 :
		print("D ")
	if ce == 0 :
		print("E ")
	if cf == 0 :
		print("F ")
	if cg == 0 :
		print("G ")
	if ch == 0 :
		print("H ")
	return

def semaforo():
	esto = [[1,0,1,0,1,0,0,0],[0,1,0,1,0,1,0,0],[1,0,1,0,0,0,1,0],[0,1,0,1,0,0,0,1],[1,0,0,0,1,0,1,0],[0,1,0,0,0,1,0,1],[0,0,1,0,1,0,1,0],[0,0,0,1,0,1,0,1]]
	car1 = random.randint(0, 15)
	car2 = random.randint(0, 15)
	car3 = random.randint(0, 15)
	car4 = random.randint(0, 15)
	car5 = random.randint(0, 15)
	car6 = random.randint(0, 15)
	car7 = random.randint(0, 15)
	car8 = random.randint(0, 15)
	while True:
		for i in range(0,7):
			for j in range (0,15):
				if esto[i][0] == 1 and car1 > 0 :
					car1 = car1 - 1
				if esto[i][1] == 1 and car2 > 0 :
					car2 = car2 - 1
				if esto[i][2] == 1 and car3 > 0 :
					car3 = car3 - 1
				if esto[i][3] == 1 and car4 > 0 :
					car4 = car4 - 1
				if esto[i][4] == 1 and car5 > 0 :
					car5 = car5 - 1
				if esto[i][5] == 1 and car6 > 0 :
					car6 = car6 - 1
				if esto[i][6] == 1 and car7 > 0 :
					car7 = car7 - 1
				if esto[i][7] == 1 and car8 > 0 :
					car8 = car8 - 1
				print("\nCarriles en Semaforo en Verde: ")
				carriltr(esto[i][0],esto[i][1],esto[i][2], esto[i][3],esto[i][4],esto[i][5],esto[i][6],esto[i][7])
				print("\nEsperen su luz: ")
				carriltr2(esto[i][0],esto[i][1],esto[i][2], esto[i][3],esto[i][4],esto[i][5],esto[i][6],esto[i][7])
				print("\n\nCarril A: %d Carril B: %d \n" % (car1, car2))
				print("Carril C: %d Carril D: %d \n" % (car3, car4))
				print("Carril E: %d Carril F: %d \n" % (car5, car6))
				print("Carril G: %d Carril H: %d \n\n\n" % (car7, car8))
				sleep(0.5)
				clear()
				
			car1 = random.randint(0, 7) + car1
			car2 = random.randint(0, 7) + car2
			car3 = random.randint(0, 7) + car3
			car4 = random.randint(0, 7) + car4
			car5 = random.randint(0, 7) + car5
			car6 = random.randint(0, 7) + car6
			car7 = random.randint(0, 7) + car7
			car8 = random.randint(0, 7) + car8
	return			

print("Semaforo en Python\n")
print("\nPresione para iniciar")
input()
clear()
semaforo()
