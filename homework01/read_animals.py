import json 
import random

with open('animals.json', 'r') as f:
    animals = json.load(f) 

rand_index = random.randint(0,19) # generate random index from 0 to 19

print(animals['animals'][rand_index]) # print random animal 


