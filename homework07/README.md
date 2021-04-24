# Tarini Thiagarajan's Homework 07 Description

The purpose of this project is to deploy a worker to k8s. 

## Installation

Install this project by cloning the repository. Change directory to access the files. For example:

```bash
git clone https://github.com/tarinit2000/tt25926_coe332.git
cd tt25926_coe332/
cd homework07/
```

## Running the Code

### Part A: 

Step 1) I fixed the Dockerfile. Then, I built a Docker image and pushed it to Docker Hub:
```bash
docker build -t tarinit2000/tarinit-test-flask-updated:1.0 .
docker push tarinit2000/tarinit-test-flask-updated:1.0 
```

Step 2) I used the file ```tarinit-hw7-flask-deployment.yml```. You can use this command to create the deployment: 
```bash
kubectl apply -f tarinit-hw7-flask-deployment.yml
```
Here's the output of the above command: ```deployment.apps/tarinit-hw7-flask-deployment created```


I used the file ```tarinit-hw7-worker-deployment.yml```. You can use this command to create the deployment: 
```bash
kubectl apply -f tarinit-hw7-worker-deployment.yml
```
Here's the output of the above command: ```deployment.apps/tarinit-hw7-worker-deployment created```

Step 3) To verify that the flask API and worker are working properly,
let's post a job:
```bash
$ kubectl exec -it redis-client-debug-deployment-5f88f47c96-mnzhj -- /bin/bash
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "aa5d540f-b548-4f8d-9155-ac2c6e5ba7d8", "status": "submitted", "start": "START TEST", "end": "END TEST"}
```
In a different terminal:
```bash
$ kubectl exec -it redis-client-debug-deployment-5f88f47c96-mnzhj -- /bin/bash
# ipython
In [1]: import redis
In [2]: rd = redis.StrictRedis(host='10.100.138.84', port=6379, db=0)
In [3]: for key in rd.keys():
   ...:     print(rd.hgetall(key))
{b'id': b'aa5d540f-b548-4f8d-9155-ac2c6e5ba7d8', b'status': b'in progress', b'start': b'START TEST', b'end': b'END TEST'}
In [4]: for key in rd.keys():
   ...:     print(rd.hgetall(key))
{b'id': b'aa5d540f-b548-4f8d-9155-ac2c6e5ba7d8', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
```
Let's try posting another job:
```bash
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "80c0a9db-bd0c-457f-9a31-2404604999b9", "status": "submitted", "start": "START TEST", "end": "END TEST"}
```
In the other terminal: 
```bash
In [5]: for key in rd.keys():
    ...:     print(rd.hgetall(key))
{b'id': b'80c0a9db-bd0c-457f-9a31-2404604999b9', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'aa5d540f-b548-4f8d-9155-ac2c6e5ba7d8', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
```
The status for both jobs is successfully submitted and completes.
      
### Part B:
I added an environment variable that stores the worker's IP address. I updated my jobs.py and worker.py to save the worker's IP address as a new key in the job record. 

Let's post a job:
```bash
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "11632897-6c84-4c8f-861d-e3b76cacb43d", "status": "submitted", "start": "START TEST", "end": "END TEST"}
```
Let's see the if the worker IP address was saved!
```bash
In [15]: for key in rd.keys():
    ...:     print(rd.hgetall(key))
{b'id': b'11632897-6c84-4c8f-861d-e3b76cacb43d', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.5.57'}
```

This looks good! The worker's IP address was saved under the "worker" key in the job record successfully. 

### Part C: 
I scaled my worker deployment to 2 pods and ran this statement to apply the change: ```kubectl apply -f tarinit-hw7-worker-deployment.yml```

Let's curl 10 jobs!
```bash
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "b58e1cb0-b1ce-47a6-8d7c-b2b64ce0696c", "status": "submitted", "start": "START TEST", "end": "END TEST"}
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "f0e25fb4-acbc-4b2a-9859-85d6ffe57a27", "status": "submitted", "start": "START TEST", "end": "END TEST"}
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "4c0409cc-38db-49e2-b3ba-f472a5fa7eee", "status": "submitted", "start": "START TEST", "end": "END TEST"}
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "c0e2c58f-441c-4c17-aa1c-72f3cff3a386", "status": "submitted", "start": "START TEST", "end": "END TEST"}
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "5c8e96e1-1d0f-493a-8986-2a029ddd9dad", "status": "submitted", "start": "START TEST", "end": "END TEST"}
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "5fc5cb7d-d2c3-47bd-a2ab-4cc1127a5bfa", "status": "submitted", "start": "START TEST", "end": "END TEST"}
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "b74280fe-8f65-46ce-af83-41d528c3d1ec", "status": "submitted", "start": "START TEST", "end": "END TEST"}
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "26399f84-c394-4fc1-a79b-f09290cb2ced", "status": "submitted", "start": "START TEST", "end": "END TEST"}
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "cdc2e39d-577e-47f9-8184-f45236bfa928", "status": "submitted", "start": "START TEST", "end": "END TEST"}
# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.244.13.47:5000/jobs
{"id": "ebea3fe3-4c19-4571-81d9-77d05e7a5fda", "status": "submitted", "start": "START TEST", "end": "END TEST"}
```
Let's check the worker IP address for each job!
```bash
In [19]: for key in rd.keys():
    ...:     print(rd.hgetall(key))
{b'id': b'b74280fe-8f65-46ce-af83-41d528c3d1ec', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.5.57'}
{b'id': b'5fc5cb7d-d2c3-47bd-a2ab-4cc1127a5bfa', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.15.72'}
{b'id': b'c0e2c58f-441c-4c17-aa1c-72f3cff3a386', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.15.72'}
{b'id': b'26399f84-c394-4fc1-a79b-f09290cb2ced', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.15.72'}
{b'id': b'5c8e96e1-1d0f-493a-8986-2a029ddd9dad', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.5.57'}
{b'id': b'f0e25fb4-acbc-4b2a-9859-85d6ffe57a27', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.15.72'}
{b'id': b'cdc2e39d-577e-47f9-8184-f45236bfa928', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.5.57'}
{b'id': b'4c0409cc-38db-49e2-b3ba-f472a5fa7eee', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.5.57'}
{b'id': b'ebea3fe3-4c19-4571-81d9-77d05e7a5fda', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.15.72'}
{b'id': b'b58e1cb0-b1ce-47a6-8d7c-b2b64ce0696c', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker': b'10.244.5.57'}
```
Interestingly, each worker pod did 5 out of 10 jobs! The work was split evenly. 

