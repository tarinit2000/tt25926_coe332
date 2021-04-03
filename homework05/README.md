# Tarini Thiagarajan's Homework 05 Description

The purpose of this project is to work with kubernetes (pods and deployments).

## Installation

Install this project by cloning the repository. Change directory to access the files. For example:

```bash
git clone https://github.com/tarinit2000/tt25926_coe332.git
cd tt25926_coe332/
cd homework05/
```

## Running the Code

### PART A: Create a pod in Kubernetes to print a Hello message!

  1) I used the file ```pod-partA.yml``` for Part A. You can use this command to create the pod:
     ```bash 
     kubectl apply -f pod-partA.yml
     ```
        
  2) You can use this command to get the pod using the following selector:
        ```bash
        kubectl get pods  --selector "greeting=personalized" 
        ```
        Here's the output of the above command: 
        ```bash
        NAME        READY   STATUS    RESTARTS   AGE
        tarini-hw   1/1     Running   0          4m2s   
        ```
         
  3) Use this command to check the logs of the pod: 
        ```bash
        kubectl logs tarini-hw 
        ```
        Here's the output of the above command: ```Hello, !``` I expected the above output since we still have not assigned the NAME variable a value.
        
  4) Use this command to delete the pod: 
      ```bash
      kubectl delete pods tarini-hw
      ```
      
### PART B: Create a pod in Kubernetes to print "Hello, $Name" using an environment variable!

  1) I used the file ```pod-partB.yml``` for Part B. You can use this command to create the pod: 
     ```bash
     kubectl apply -f pod-partB.yml
     ```
     
  2) You can use this command to check the logs of the pod: 
     ```bash
     kubectl logs tarini-hw-partb
     ```
     Here's the output of the above command: 
     ```Hello, Tarini Thiagarajan!```
     
  3) You can use this command to delete the pod: 
     ```bash
     kubectl delete pods tarini-hw-partb
     ```

Part C: 
  1) I used this file ```deployment-partC.yml``` for Part C. You can use this command to create the deployment:
 
    ``` 
    kubectl apply -f deployment-partC.yml 
    ``` 
    
  2) You can use this command to get all the pods in the deployment and their IP address: 

    ```
    kubectl get pods -o wide 
    ```
    
    Here's the output of the above comand:  
    ```
    NAME                                    READY   STATUS    RESTARTS   AGE     IP              NODE                         NOMINATED NODE   READINESS GATES
    tarini-hw-partc-68f7bf8cfb-54jpd        1/1     Running   0          54s     10.244.6.115    c03                          <none>           <none>
    tarini-hw-partc-68f7bf8cfb-98vgw        1/1     Running   0          56s     10.244.3.243    c01                          <none>           <none>
    tarini-hw-partc-68f7bf8cfb-sv9tx        1/1     Running   0          53s     10.244.4.120    c02                          <none>           <none>
    ```
    
  3) The logs associated with each pod in the deployment match the output from number 2, as expected!
    ```
    $ kubectl logs tarini-hw-partc-68f7bf8cfb-54jpd
    Hello, Tarini Thiagarajan from IP 10.244.6.115!
    [tarinit@isp02 homework05]$ kubectl logs tarini-hw-partc-68f7bf8cfb-98vgw
    Hello, Tarini Thiagarajan from IP 10.244.3.243!
    [tarinit@isp02 homework05]$ kubectl logs tarini-hw-partc-68f7bf8cfb-sv9tx
    Hello, Tarini Thiagarajan from IP 10.244.4.120!
    ```
