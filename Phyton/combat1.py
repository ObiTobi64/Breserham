import random

dodge_prob = 0.5

iteraciones = 10
contador = 0

for i in range(iteraciones):
    if random.random () < dodge_prob:
        print('esquiva')
    else:
        print('ouch')