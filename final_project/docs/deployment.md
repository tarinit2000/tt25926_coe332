# Tarini Thiagarajan's Final Project Deployment Description

This file will walk you through deploying the system on a Kubernetes cluster. 

## Building a docker image

Build a docker image and push it to Docker Hub using a format similar to this:

```bash
docker build -t tarinit2000/tarinit-finalproj-app-flask:1.0 .
docker push tarinit2000/tarinit-finalproj-app-flask:1.0 
```

## Deploying the System on a Kubernetes Cluster

### Deploy: 

I used the file ```tarinit-finalproj-flask-deployment.yml```. You can use this command to create the deployment: 
```bash
kubectl apply -f tarinit-finalproj-flask-deployment.yml
```
Here's the output of the above command: ```deployment.apps/tarinit-test-flask-deployment-finalproj created```

I used the file ```tarinit-finalproj-flask-service.yml```. You can use this command to create the deployment: 
```bash
kubectl apply -f tarinit-finalproj-flask-service.yml
```
Here's the output of the above command: ```service/tarinit-test-flask-service-finalproj created```

I used the file ```tarinit-finalproj-redis-deployment.yml```. You can use this command to create the deployment: 
```bash
kubectl apply -f tarinit-finalproj-redis-deployment.yml
```
Here's the output of the above command: ```deployment.apps/tarinit-test-redis-deployment-finalproj created```

I used the file ```tarinit-finalproj-redis-service.yml```. You can use this command to create the deployment: 
```bash
kubectl apply -f tarinit-finalproj-redis-service.yml
```
Here's the output of the above command: ```service/tarinit-test-redis-service-finalproj created```

I used the file ```tarinit-finalproj-redis-pvc.yml```. You can use this command to create the deployment: 
```bash
kubectl apply -f tarinit-finalproj-redis-pvc.yml
```
Here's the output of the above command: ```persistentvolumeclaim/tarinit-test-redis-pvc-finalproj created```

I used the file ```tarinit-finalproj-worker-deployment.yml```. You can use this command to create the deployment: 
```bash
kubectl apply -f tarinit-finalproj-worker-deployment.yml
```
Here's the output of the above command: ```deployment.apps/tarinit-test-worker-deployment-finalproj created```

### Check the status of the kubernetes pods

```bash
$ kubectl get pods
NAME                                                        READY   STATUS    RESTARTS   AGE
redis-client-debug-deployment-5f88f47c96-mnzhj              1/1     Running   1          22d
tarinit-test-flask-deployment-finalproj-56f856b895-zsjgf    1/1     Running   0          48m
tarinit-test-redis-deployment-finalproj-7c54bddd8c-xknbh    1/1     Running   0          47m
tarinit-test-worker-deployment-finalproj-7df8f64bbd-srdws   1/1     Running   2          49m
```

### Check the service IP addresses for future curl operations

```bash
$ kubectl get services
NAME                                   TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
tarinit-test-flask-service-finalproj   ClusterIP   10.111.234.33    <none>        5000/TCP         63m
tarinit-test-redis-service-finalproj   ClusterIP   10.104.122.228   <none>        6379/TCP      
```

### Check the pvc status

```bash
$ kubectl get pvc
NAME                               STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
tarinit-test-redis-pvc-finalproj   Bound    pvc-28c238eb-b4be-4b45-9879-2f6e425fea9a   1Gi        RWO            rbd            4d7h
```
