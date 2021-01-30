import json 
import random 
import petname

data = {} # create empty dictionary 
data['animals'] = [] # create empty list with key animals

for i in range(20): # loop through 20 animals
    head_list = ['snake', 'bull', 'lion', 'raven', 'bunny']
    rand_index = random.randint(0,4) # random index from 0 to 4
    head = head_list[rand_index]
    body = petname.name()+'-'+petname.name()
    arms = random.randrange(2,12,2) # random even number from 2 to 10 
    legs = random.randrange(3,15,3) # random multiple of 3 number from 3 to 12
    tails = arms + legs

    data['animals'].append( {'head': head, 'body': body, 'arms': arms, 
                             'legs': legs, 'tail': tails})
    
                          
with open('animals.json', 'w') as out:
    json.dump(data, out, indent=2)
