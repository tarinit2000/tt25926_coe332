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
Here's the output of the above command: ```persistentvolumeclaim/tarinit-test-redis-pvc created```
      
### Step 2: Create a deployment for the Redis database!

I used the file ```tarinit-test-redis-deployment.yml``` for Step 2. You can use this command to create the deployment: 
```bash
kubectl apply -f tarinit-test-redis-deployment.yml
```
Here's the output of the above command: ```deployment.apps/tarinit-test-redis-deployment created```
     
### Step 3: Create a service for the Redis database!

I used the file ```tarinit-test-redis-service.yml``` for Step 3. You can use this command to create the service: 
```bash
kubectl apply -f tarinit-test-redis-service.yml
```
Here's the output of the above command: ```service/tarinit-test-redis-service created```

### Checking Steps 1-3: 

Look up the service IP address for the test redis service:
```bash
$ kubectl get services
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
tarinit-test-redis-service   ClusterIP   10.100.138.84    <none>        6379/TCP         27h
```
Exec into a Python debug container, install the redis python library, launch the python shell, and import redis:
```bash 
$ kubectl exec -it py-debug-deployment-5cc8cdd65f-vbn5n -- /bin/bash
# apt-get update && apt-get install -y python3
# apt-get install python3-pip
# pip3 install redis
# python3
>>import redis
```
Create a Python redis client object using the IP and port of the service. Create a key and make sure you can get the key:
```bash
>>rd = redis.StrictRedis(host='10.100.138.84', port=6379, db=0)
>>> rd.set('test_key','it worked!')
True
>>> rd.get('test_key')
[b'it worked!']
```
In another shell on isp02, delete the redis pod. Check that k8s creates a new redis pod.
```bash
$ kubectl delete pods tarinit-test-redis-deployment-74857d6d9d-tpc5l
pod "tarinit-test-redis-deployment-74857d6d9d-tpc5l" deleted
$ kubectl get pods
NAME                                             READY   STATUS    RESTARTS   AGE
tarinit-test-redis-deployment-74857d6d9d-kncwr   1/1     Running   0          10s
```
Back in the python shell, check that you can still get the key using the same IP: 
```bash
>>> rd.get(test_key')
[b'it worked!']
```

### Step 4: Create a deployment for the flask API!

I used the file ```tarinit-test-flask-deployment.yml``` for Step 4. You can use this command to create the deployment: 
```bash
kubectl  apply -f tarinit-test-flask-deployment.yml
```
Here's the output of the above command: ```deployment.apps/tarinit-test-flask-deployment created```

### Step 5: Create a service for the flask API!

I used the file ```tarinit-test-flask-service.yml``` for Step 5. You can use this command to create the service: 
```bash
kubectl apply -f tarinit-test-flask-service.yml
```
Here's the output of the above command: ```service/tarinit-test-flask-service created```

### Checking Steps 1-3: 
Look up the pod IP address for the test flask deployment:
```bash
$ kubectl get pods -o wide tarinit-test-flask-deployment-f5c47cc9b-p9xb4
NAME                                            READY   STATUS    RESTARTS   AGE   IP             NODE   NOMINATED NODE   READINESS GATES
tarinit-test-flask-deployment-f5c47cc9b-p9xb4   1/1     Running   0          66m   10.244.4.138   c02    <none>           <none>
```
Look up the service IP address for the test flask service:
```bash
$ kubectl get services
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
tarinit-test-flask-service   ClusterIP   10.99.5.34       <none>        5000/TCP         12h
```
Check to see if you can curl both:
```bash
$ kubectl exec -it py-debug-deployment-5cc8cdd65f-vbn5n -- /bin/bash
# curl 10.244.4.138:5000
Hello World!
# curl 10.99.5.34:5000
Hello World!
```
