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

  1) I used the file ```pod-partA.yml``` for part A. You can use this command to create the pod:
     ```kubectl apply -f pod-partA.yml```
        
  2) 
        Use this command to get the pod using the following selector:
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
        Here's the output of the above comand: 
        ```bash
        Hello, !
        ```
        I expected the above output since we still have not assigned the NAME variable a value.
        
  4) Use this command to delete the pod: 
      ```bash
      kubectl delete pods tarini-hw
      ```
      
PART B) Create a pod in Kubernetes to print "Hello, $Name" using an environment variable!

  1) File: pod-partB.yml
     Use this command to create the pod: 
     ```bash
     kubectl apply -f pod-partB.yml
     ```
     
  2) Use this command to check the logs of the pod: 
     ```bash
     kubectl logs tarini-hw-partb
     ```
     Here's the output of the above comand: 
     ```bash
     Hello, Tarini-Thiagarajan! 
     ```
  3) Use this command to delete the pod: 
     ```bash
     kubectl delete pods tarini-hw-partb
     ```

Part C: 
  1) 
    File: pod-partC.yml 
    Use this command to create the deployment: 
    ```bash
    kubectl apply -f pod-partC.yml 
    ``` 
    
  2) 
    Use this command to get all the pods in the deployment and their IP address: 
    ```bash
    kubectl get pods -o wide
    ```
    Here's the output of the above comand:  
    ```bash
    NAME                                    READY   STATUS    RESTARTS   AGE     IP              NODE                         NOMINATED NODE   READINESS GATES
    tarini-hw-partc-85954b77bf-65fzp        1/1     Running   0          91s     10.244.5.82     c04                          <none>           <none>
    tarini-hw-partc-85954b77bf-9ff6f        1/1     Running   0          91s     10.244.3.214    c01                          <none>           <none>
    tarini-hw-partc-85954b77bf-n7cjl        1/1     Running   0          91s     10.244.6.107    c03                          <none>           <none>
    ```
    
  3) 
    Use this command to check the logs associated with each pod in the deployment: 
    ```bash
    kubectl logs tarini-hw-partc-85954b77bf-65fzp
    ```
    Here's the output of the above command:
    ```bash
    Hello, Tarini-Thiagarajan from IP 10.244.5.82!
    ```
    
    Use this command to check the logs associated with each pod in the deployment: 
    ```bash
    kubectl logs tarini-hw-partc-85954b77bf-9ff6f
    ```
    Here's the output of the above command: 
    ```bash
    Hello, Tarini-Thiagarajan from IP 10.244.3.214!
    ```
    
    Use this command to check the logs associated with each pod in the deployment: 
    ```bash
    kubectl logs tarini-hw-partc-85954b77bf-n7cjl
    ```
     Here's the output of the above command: 
    ```bash
    Hello, Tarini-Thiagarajan from IP 10.244.6.107!
    ```
    Yes, the logs associated with each pod in the deployment match the output from number 2 as expected!


