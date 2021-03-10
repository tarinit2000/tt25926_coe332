import json
from random import randrange
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World!\n"

@app.route('/animals', methods=['GET'])
def get_animals():
    return json.dumps(get_data(), indent=2)

@app.route('/animals/head/', methods=['GET'])
def get_animals_with_head():
    animals_dict = get_data()
    name = request.args.get('name') # user inputs 'name' and we store it as name
    output = [x for x in animals_dict if x['head'] == name]
    return json.dumps(output, indent=2)

@app.route('/animals/legs/', methods=['GET'])
def get_animals_with_legs():
    animals_dict = get_data()
    number = request.args.get('number') # user inputs 'name' and we store it as name
    output = [x for x in animals_dict if x['legs'] == int(number)] 
    return json.dumps(output, indent=2)

def get_data(): # function that reads animals.json into a dictionary
    with open("animals_data.json", "r") as f:
        animal_dict = json.load(f)
    return animal_dict
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
