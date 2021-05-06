# api.py
import json, datetime, load, redis
from flask import Flask, request, send_file
from jobs import rd_job, rd_data, q, get_data, add_job, generate_job_key

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World!\n"

@app.route('/reset/', methods=['GET'])
def reset_data():
   #load.csvtojson() # converts csv to json from load.py file
    with open("data.json", "r") as f:
        patients_dict = json.load(f)
    rd_data.set('patients_key', json.dumps(patients_dict))
    return 'Database has been reset!\n'

@app.route('/info/', methods=['GET'])
def get_info():
    return """
    Try these routes: 

    /                   "Hello World!" connection test
    /reset/             Reset the patient database 
    /patients/all/      (GET) View all patients in database
    /patients/add/      (POST) Add a patient to the database
    /patients/delete/   (GET) Remove a patient from the database
    /patients/edit/     (GET) Edit a patient's information
    /subject/id/        (GET) Get a patient with a certain id
    /summary/           (GET) Get a summary of the patient database
    /scans/             (GET) Start a job to plot patient data over a range of time
    /jobs/all/          (GET) Get a list of all jobs
    /jobs/id/           (GET) Get information for a specific job given a jobid
    /download/          (GET) Download plot image
    /jobs/delete/all/   Delete all jobs from the job database

"""

@app.route('/patients/all/', methods=['GET'])
def get_patients():
    return json.dumps(get_data(), indent=2)

@app.route('/patients/add/', methods=['POST'])
def add_patient():
    try:
        add_this_patient = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    
    patients_dict = get_data()
    patients_dict['patients'].append(add_this_patient)
    rd_data.set('patients_key', json.dumps(patients_dict))
    return json.dumps(get_data(), indent=2)

@app.route('/patients/delete/', methods=['GET'])
def del_patient():
    patients_dict = get_data()
    uuid = request.args.get('id') # user inputs 'id' and we store it as id
    for x in patients_dict['patients']:
        if x['id'] == uuid:
            patients_dict['patients'].remove(x)
    
    rd_data.set('patients_key', json.dumps(patients_dict))
    return 'Patient was deleted'

@app.route('/patients/edit/', methods=['GET'])
def edit_patient():
    patients_dict = get_data()
    uuid = request.args.get('id')
    scan1 = request.args.get('Scan1') 
    scan2 = request.args.get('Scan2')
    scan3 = request.args.get('Scan3')
    scan4 = request.args.get('Scan4') 
    scan5 = request.args.get('Scan5') 
    scan6 = request.args.get('Scan6') 
    scan7 = request.args.get('Scan7') 
    scan8 = request.args.get('Scan8') 
    scan9 = request.args.get('Scan9') 
    scan10 = request.args.get('Scan10') 
    patient = {}
    for x in patients_dict['patients']:
        if x['id'] == uuid:
            x['Scan 1'] = scan1
            x['Scan 2'] = scan2
            x['Scan 3'] = scan3
            x['Scan 4'] = scan4
            x['Scan 5'] = scan5
            x['Scan 6'] = scan6
            x['Scan 7'] = scan7
            x['Scan 8'] = scan8
            x['Scan 9'] = scan9
            x['Scan 10'] = scan10
            patient = x
    
    rd_data.set('patients_key', json.dumps(patients_dict))
    return json.dumps(patient, indent=2)
  
@app.route('/subject/id/', methods=['GET'])
def get_patient_with_id():
    patients_dict = get_data()
    output = {}
    uuid = request.args.get('id') # user inputs 'id' and we store it as id
    for x in patients_dict['patients']:
        if x['id'] == uuid:
            output = x
    return json.dumps(output, indent=2)
   
@app.route('/summary/', methods=['GET'])
def get_summary():
    output = {}
    data = get_data()
    patients = []
    count = 0
    scan = 0
    for p in data['patients']:
        if p['Scan 1'] != None:
            count = count + 1
            scan = scan + 1
        if p['Scan 2'] != None:
            count = count + 1
            scan = scan + 1
        if p['Scan 3'] != None:
            count = count + 1
            scan = scan + 1
        if p['Scan 4'] != None:
            count = count + 1
            scan = scan + 1
        if p['Scan 5'] != None:
            count = count + 1
            scan = scan + 1
        if p['Scan 6'] != None:
            count = count + 1
            scan = scan + 1
        if p['Scan 7'] != None:
            count = count + 1
            scan = scan + 1
        if p['Scan 8'] != None:
            count = count + 1
            scan = scan + 1
        if p['Scan 9'] != None:
            count = count + 1
            scan = scan + 1
        if p['Scan 10'] != None:
            count = count + 1
            scan = scan + 1
    
        if scan >= 5:
            patients.append(p['id'])
            
        scan = 0 
    
    output['Number of patients in total:'] = str(len(data['patients']))
    output['Number of non-Null readings in total:'] = str(count)
    output['Patients with at least 5 non-Null readings:'] = patients

    return json.dumps(output, indent=2)

@app.route('/scans/', methods=['GET'])
def get_scans_between():
    start = request.args.get('start')
    end = request.args.get('end')
    return json.dumps(add_job(start,end))

@app.route('/jobs/all/', methods=['GET'])
def get_jobs():
    jobs_dict = {}
    for key in rd_job.keys():
        jobs_dict[str(key.decode('utf-8'))] = {}
        jobs_dict[str(key.decode('utf-8'))]['status'] = rd_job.hget(key, 'status').decode('utf-8')
        jobs_dict[str(key.decode('utf-8'))]['id'] = rd_job.hget(key, 'id').decode('utf-8')
    return json.dumps(jobs_dict, indent=2)

@app.route('/jobs/id/', methods=['GET'])
def get_outputof_job():
    jobuuid = request.args.get('jobuuid')
    bytes_dict = rd_job.hgetall(generate_job_key(jobuuid))

    output = {}
    for key, value in bytes_dict.items():
        if key.decode('utf-8') == 'image':
            output[key.decode('utf-8')] = 'ready'
        else:
            output[key.decode('utf-8')] = value.decode('utf-8')
    return json.dumps(output, indent=2)

@app.route('/download/', methods=['GET'])
def download():
    jobuuid = request.args.get('jobuuid')
    a = '/api/'
    b = str(jobuuid)
    c =  '.png'
    path = a+b+c # this results in: '/api/{jobuuid}.png'
    with open(path, 'wb') as f:
        f.write(rd_job.hget(generate_job_key(jobuuid), 'image'))
    return send_file(path, mimetype='image/png', as_attachment=True)

@app.route('/jobs/delete/all/', methods=['GET'])
def del_jobs():
    for x in rd_job.keys():
        rd_job.delete(x)
    return 'All jobs were cleared.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
