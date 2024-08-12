#COMBATE ENTRE DOS PERSONAJES
#Nivel definido de HP
#Daño definido por ataque normal 
#Probabilidad de esquivar un ataque normal 
#Ataque especial con daño critico
#Cuando el nivel de HP llegue a un valor menor o igual a 0 el personake muere 

import random 


prob_esquivar = random.random()

Hp1 = 100
Hp2 = 100

def daño (damage):
    
    global Hp1,Hp2
    Hp1 = Hp1 - damage
    Hp2 = Hp2 - damage
    print(f"Hp1: {Hp1}")
    print(f"Hp2: {Hp2}")

daño(int(input('Ingrese el danio: ')))











