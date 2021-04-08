# Tarini Thiagarajan's Homework 05 Description

The purpose of this project is to create a “test” environment for our Flask API application.

## Installation

Install this project by cloning the repository. Change directory to access the files. For example:

```bash
git clone https://github.com/tarinit2000/tt25926_coe332.git
cd tt25926_coe332/
cd homework06/
```

## Running the Code

### Step 1: Create a persistent volume claim for the Redis data!

I used the file ```tarinit-test-redis-pvc.yml``` for Step 1. You can use this command to create the pvc:
```bash 
kubectl apply -f tarinit-test-redis-pvc.yml
```
Here's the output of the above command:
```bash
persistentvolumeclaim/tarinit-test-redis-pvc created
```
      
### Step 2: Create a deployment for the Redis database!

I used the file ```tarinit-test-redis-deployment.yml``` for Step 2. You can use this command to create the pod: 
```bash
kubectl apply -f tarinit-test-redis-deployment.yml
```
Here's the output of the above command: 
```bash
deployment.apps/tarinit-test-redis-deployment created
```
     
### Step 3: Create a service for the Redis database!

I used the file ```tarinit-test-redis-service.yml``` for Step 3. You can use this command to create the pod: 
```bash
kubectl apply -f tarinit-test-redis-service.yml
```
Here's the output of the above command: 
```bash
service/tarinit-test-redis-service created
```

### Checking Steps 1-3: 

```bash
$ kubectl get services
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
tarinit-test-redis-service   ClusterIP   10.100.138.84    <none>        6379/TCP         27h
```

$ kubectl exec -it py-debug-deployment-5cc8cdd65f-vbn5n -- /bin/bash
# apt-get update && apt-get install -y python3
# apt-get install python3-pip
# pip3 install redis
# python3
>>import redis
>>rd = redis.StrictRedis(host='10.100.138.84', port=6379, db=0)
>>> rd.set('test_key','it worked!')
True
>>> rd.get('test_key')
[b'it worked!']

In a different window: 
$ kubectl delete pods tarinit-test-redis-deployment-74857d6d9d-tpc5l

In the previous exec window: 
>>> rd.get(test_key')
[b'it worked!']



### Step 4: Create a deployment for the flask API!

I used the file ```tarinit-test-flask-deployment.yml``` for Step 4. You can use this command to create the pod: 
```bash
kubectl  apply -f tarinit-test-flask-deployment.yml
```
Here's the output of the above command: 
```bash
deployment.apps/tarinit-test-flask-deployment created
```

### Step 5: Create a service for the flask API!

I used the file ```tarinit-test-flask-service.yml``` for Step 5. You can use this command to create the pod: 
```bash
kubectl apply -f tarinit-test-flask-service.yml
```
Here's the output of the above command: 
```bash
service/tarinit-test-flask-service created
```
