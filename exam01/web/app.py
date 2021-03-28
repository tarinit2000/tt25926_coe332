import json
import datetime 
import redis
from random import randrange
from flask import Flask, request

rd = redis.StrictRedis(host='redis', port=6379, db=0)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World!\n"

@app.route('/animals/', methods=['GET'])
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

@app.route('/reset/', methods=['GET'])
def reset_data():
    with open("animals.json", "r") as f:
        animal_dict = json.load(f)
    rd.set('tarini-animals', json.dumps(animal_dict))
    return 'Database has been reset!\n'

@app.route('/animals/dates/', methods=['GET'])
def get_all_within_dates():
    animals_dict = get_data()
    d1 = request.args.get('start_date')
    d2 = request.args.get('end_date')

    dt1_obj = datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M:%S.%f')  
    dt2_obj = datetime.datetime.strptime(d2, '%Y-%m-%d %H:%M:%S.%f')
    
    output = []
    for x in animals_dict:
        xdate = datetime.datetime.strptime(x['created_on'], '%Y-%m-%d %H:%M:%S.%f')
        if dt1_obj <= xdate <= dt2_obj:
            output.append(x)

    return json.dumps(output, indent=2)

@app.route('/animals/uid/', methods=['GET'])
def get_animal_with_uid():
    animals_dict = get_data()
    uid = request.args.get('uid')
    output = [x for x in animals_dict if x['uid'] == uid] 
    return json.dumps(output, indent=2)

@app.route('/animals/uidedit/', methods=['GET'])
def edit_animal_with_uid():
    animals_dict = get_data()
    uid = request.args.get('uid')
    uid_new = request.args.get('uid_new')
    head = request.args.get('head')
    body = request.args.get('body')
    arms = request.args.get('arms')
    legs = request.args.get('legs')
    tail = request.args.get('tail')
    date = request.args.get('date')
            
    for i in range(len(animals_dict)):
        if animals_dict[i]['uid'] == uid:
            animals_dict[i]['head'] = head
            animals_dict[i]['body'] = body
            animals_dict[i]['arms'] = int(arms)
            animals_dict[i]['legs'] = int(legs)
            animals_dict[i]['tail'] = int(tail)
            animals_dict[i]['created_on'] = date
            animals_dict[i]['uid'] == uid_new
            break

    rd.set('tarini-animals', json.dumps(animals_dict))
    return json.dumps(get_data(), indent=2)

@app.route('/animals/delete/', methods=['GET'])
def get_range_of_dates():
    animals_dict = get_data()
    d1 = request.args.get('start_date')
    d2 = request.args.get('end_date')
    dt1_obj = datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M:%S.%f')  
    dt2_obj = datetime.datetime.strptime(d2, '%Y-%m-%d %H:%M:%S.%f')

    to_remove = []
    for x in animals_dict:
        xdate = datetime.datetime.strptime(x['created_on'], '%Y-%m-%d %H:%M:%S.%f')
        if dt1_obj <= xdate <= dt2_obj:
            to_remove.append(x)
    for x in to_remove:
        animals_dict.remove(x)

    rd.set('tarini-animals', json.dumps(animals_dict))
    return json.dumps(get_data(), indent=2)

@app.route('/animals/avglegs/', methods=['GET'])
def get_avg_snake_legs():
    animals_dict = get_data()
    sum = 0
    for x in animals_dict:
       sum = sum + int(x['legs'])
    avg = sum/len(animals_dict)
    return "Average of all legs = " + str(avg) + "\n"

@app.route('/animals/totalcount/', methods=['GET'])
def get_total_num_animals():
    animals_dict = get_data()
    return "Total count of animals: " + str(len(animals_dict)) + "\n"

def get_data():
     return json.loads(rd.get('tarini-animals').decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # default port 5000
