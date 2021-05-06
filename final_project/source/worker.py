from jobs import q, update_job_status, rd_data, get_data, generate_job_key
import matplotlib.pyplot as plt
from redis import StrictRedis
rd_job = StrictRedis(host='10.104.122.228', port=6379, db=0)
@q.worker
def execute_job(jid):
    jobid, status, start, end = rd_job.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end')
    
    if type(jid) == str:
        job = {'id': jid,
               'status': status,
               'start': start,
               'end': end
        }
    else: 
        job = {'id': jid.decode('utf-8'),
               'status': status.decode('utf-8'),
               'start': start.decode('utf-8'),
               'end': end.decode('utf-8')
        }

    if job:
        job['status'] = 'in progress'
        rd_job.hmset(generate_job_key(job['id']), job)
    else:
        raise Exception()

    start = job['start']
    end = job['end']

    keys = []
    first = int(start[-2:]) # first scan number
    last = int(end[-2:]) # last scan number
    for x in range(first, last+1):
        key = 'Scan ' + str(x)
        keys.append(key) # range of keys (aka scans) the user wants to plot 
    output = {}
    output['x'] = []
    output['y'] = []
 
    x_iter = range(0,72+8,8) # 10 scans every 8 weeks over 72 week period
    count = 0
    patients_dict = get_data()
    for i in keys:
        for x in patients_dict['patients']:
            if x[i] != None:
                output['y'].append(float(x[i]))
                output['x'].append(x_iter[count])
        count = count + 1
    
    rd_job.hset(generate_job_key(jid), 'x-y results', 'passed')

    last_xtick = output['x'][-1] # last date
    xticks_list = range(0,last_xtick+8,8)

    plt.scatter(output['x'],output['y'], s=10)
    plt.xlabel('Time (weeks)')
    plt.ylabel('Tumor Diameters (mm)')
    plt.xticks(xticks_list)
    #plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])
    plt.title('Tumor Progression Over Time')
    plt.savefig('out.png')
    
    with open('out.png', 'rb') as f:
        img = f.read()
        
    rd_job.hset(generate_job_key(jid), 'image', img)

    jobid, status, start, end = rd_job.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end')
    
    if type(jid) == str:
        job = {'id': jid,
               'status': status,
               'start': start,
               'end': end
        }
    else: 
        job = {'id': jid.decode('utf-8'),
               'status': status.decode('utf-8'),
               'start': start.decode('utf-8'),
               'end': end.decode('utf-8')
        }

    if job:
        job['status'] = 'complete'
        rd_job.hmset(generate_job_key(job['id']), job)
    else:
        raise Exception()

execute_job() # worker will run as daemon
