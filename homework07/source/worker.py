from jobs import q, update_job_status, set_workerIP
import time 
import os 

worker_ip = os.environ.get('WORKER_IP')
if not worker_ip:
    raise Exception()

@q.worker
def execute_job(jid):
    # fill in and added it
    update_job_status(jid, 'in progress')
    set_workerIP(jid, worker_ip)
    # do actual work
    time.sleep(15)
    update_job_status(jid, 'complete')

execute_job() # worker will run as daemon
