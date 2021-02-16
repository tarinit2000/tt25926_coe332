#!/usr/bin/env python3
import json
import random
import sys

def breed(mom, dad):
    child = {}
    child['head'] = random.choice([mom['head'], dad['head']]) 
    dad_body = random.choice(dad['body'].split('-')) 
    mom_body = random.choice(mom['body'].split('-'))
    child['body'] = mom_body + '-' + dad_body
    child['arms'] = random.choice([mom['arms'], dad['arms']])
    child['legs'] = random.choice([mom['legs'], dad['legs']])
    child['tail'] = random.choice([mom['tail'], dad['tail']])
    return child
  
def main():
    with open(sys.argv[1], 'r') as f:
        animal_dict = json.load(f)
        
    random_indices = random.sample(range(0,20),2)
    parent1 = animal_dict['animals'][random_indices[0]]
    parent2 = animal_dict['animals'][random_indices[1]]
    
    print('Mom')
    print(parent1)
    print('Dad')
    print(parent2)
    print('Child:')
    child = breed(parent1, parent2)
    print(child)
    print('Random animal:')
    print(random.choice(animal_dict['animals']))    

if __name__ == '__main__':
    main()
