# Tarini Thiagarajan's Final Project User Description
This file will walk you through how to interact with this API. 

## What is Glioblastoma?
Glioblastoma is the most invasive and common form of brain tumor in adults globally, and current treatments are ineffective in targeting all cancerous cells. 
To understand the nature of this disease, glioblastoma progresses when brain cells called astrocytes mutate and spread uncontrollably throughout the entire brain. 
These cancer cells damage healthy brain tissue and increase pressure on surrounding tissue and the skull. 
Glioblastoma symptoms include a significant deterioration in natural cognitive functions, severe headaches, and frequent seizures. 
Unfortunately, this invasive disease has no known cure and has extremely low prognosis (median survival timeline of fifteen to eighteen months and a 10% five-year survival rate).

## Project Data
### Information about the Data 
The data set for this project was derived from: https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=50135264#501352644613f7d5a2514c2195445afde60ce068
In the research study linked above, 123 glioblastoma patients had MRI scans done every 8 weeks for 72 weeks (10 total scans). 
For the purposes of this project, the data dictionary stores the cross-sectional tumor diameters, a common means for characterizing tumors in the clinic, for all patients. 
Additionally, patients with zero baseline diameters and no scans after baseline were removed from the data set since they did not have enough insightful data.
Thus, 62 patients remained for analysis. 

### Converting the Data from CSV to JSON
The ```load.py``` file was used to convert the csv raw data into a ```data.json``` file. Patients without data for certain scans were given a value of "null", and each patient was assigned a uuid for identification purposes in the ```load.py``` file. 
The load.py can be run by:
```bash 
python3 load.py
```
The above command adds a ```data.json``` file to the local directory with the glioblastoma patient data stored as a json dictionary. 

## Running the Project 
### Flask 
#### CRUD Operations
Exec into the worker deployment using this code:
```bash
$ kubectl exec -it tarinit-test-worker-deployment-finalproj-7df8f64bbd-srdws -- /bin/bash
```
Now, you can start curling routes! Let's start with a simple test.
```bash
# curl 10.111.234.33:5000/
Hello World!
```
Great! Now, curl the /info/ route in order to get more information about the routes you can curl.
``` bash
# curl 10.111.234.33:5000/info/
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

```
Here are some example curl routes and outputs:
```bash 
# curl 10.111.234.33:5000/reset/
Database has been reset!
# curl 10.111.234.33:5000/patients/all/
{
  "patients": [
	    {
      "id": "bd156a14-f3d8-4cc9-9445-0f235033a76a",
      "Scan 1": "1",
      "Scan 2": "6.148148148",
      "Scan 3": null,
      "Scan 4": null,
      "Scan 5": null,
      "Scan 6": null,
      "Scan 7": null,
      "Scan 8": null,
      "Scan 9": null,
      "Scan 10": null
    },
    ...
    ...
    ...
  ]
}
# curl 10.111.234.33:5000/summary/
{
  "Number of patients in total:": "62",
  "Number of non-Null readings in total:": "231",
  "Patients with at least 5 non-Null readings:": [
    "dbd22a91-65c3-47f0-aeb4-0dbff91aa8a0",
    "5d68519b-b445-4442-9039-4a4db15b40bc",
    "5e17a4cd-ad82-4aba-8cfb-bddecf1d9211",
    "ddd2f5f4-aa6a-46be-b65f-baf9c968fe8e",
    "49232ff5-cde1-4946-a9c5-6a63f2ca104c",
    "f9a08f64-94fb-4761-bda4-250842d93c8e",
    "f8d868f9-8877-4737-8c19-8e37ab1e3eaa",
    "9bdd7ee9-a00a-43eb-894a-5b0285fbc925",
    "b6458a38-2fb3-4558-b4fd-a01890b9afdd",
    "37a6c8ef-1d73-425d-81c1-d647ce51fd24",
    "e7d85b92-b9ae-4578-9262-42359a996e07",
    "51c3ab69-8764-44b8-92f8-a8c091213a89",
    "115de620-eaa6-46b5-bd6b-b74166ca5f38",
    "dd6034b6-6d47-4adb-a3e7-a939fa69ab7e",
    "e159f0f7-e6a8-4968-9014-ea0ec1319f95",
    "487820e5-8fb0-4d8a-b340-a4be4c9a5448",
    "0a742a76-2305-422c-8cce-3178ffb39db0",
    "55928056-5b0b-4c25-84fe-afe5a34c1c00"
  ]
}
# curl -X POST -H "content-type: application/json" -d '{"id": "NEW_PATIENT", "Scan 1": "1", "Scan 2": "1", "Scan 3": "1", "Scan 4": "1", "Scan 5": "1", "Scan 6": "1", "Scan 7": "1", "Scan 8": "1", "Scan 9": "1", "Scan 10": "1"}' 10.111.234.33:5000/patients/add/
{
  "patients": [
	...
	...
	...
    {
      "id": "NEW_PATIENT",
      "Scan 1": "1",
      "Scan 2": "1",
      "Scan 3": "1",
      "Scan 4": "1",
      "Scan 5": "1",
      "Scan 6": "1",
      "Scan 7": "1",
      "Scan 8": "1",
      "Scan 9": "1",
      "Scan 10": "1"
    }
  ]
}
# curl '10.111.234.33:5000/subject/id/?id=002eb201-11ae-4794-ad88-06a2989a200a'
{
  "id": "002eb201-11ae-4794-ad88-06a2989a200a",
  "Scan 1": "1",
  "Scan 2": "0.915865385",
  "Scan 3": null,
  "Scan 4": null,
  "Scan 5": null,
  "Scan 6": null,
  "Scan 7": null,
  "Scan 8": null,
  "Scan 9": null,
  "Scan 10": null
}
# curl '10.111.234.33:5000/patients/edit/?id=002eb201-11ae-4794-ad88-06a2989a200a&Scan1=1.1&Scan2=1.1&Scan3=1.1&Scan4=1.1&Scan5=1.1&Scan6=1.1&Scan7=1.1&Scan8=1.1&Scan9=1.1&Scan10=1.1'
{
  "id": "002eb201-11ae-4794-ad88-06a2989a200a",
  "Scan 1": "1.1",
  "Scan 2": "1.1",
  "Scan 3": "1.1",
  "Scan 4": "1.1",
  "Scan 5": "1.1",
  "Scan 6": "1.1",
  "Scan 7": "1.1",
  "Scan 8": "1.1",
  "Scan 9": "1.1",
  "Scan 10": "1.1"
}
# curl '10.111.234.33:5000/patients/delete/?id=002eb201-11ae-4794-ad88-06a2989a200a'
Patient was deleted
```
#### Jobs Analysis (plotting patient data)
You can post a job in order to plot patient data. 
To elaborate, you can send in a start date (ex: 'Scan 1', which is week 0 or the baseline scan) and an end date (ex: 'Scan 5').
Then, a plot of this range of scans (cross-sectional tumor diameters (mm) vs time (weeks)) will be sent to your local directory. 

Here is some example curl routes and outputs:
```bash
$ kubectl exec -it tarinit-test-worker-deployment-finalproj-7df8f64bbd-srdws -- /bin/bash
# curl '10.111.234.33:5000/scans/?start=Scan%201&end=Scan%2010'
{"id": "5afb2872-a428-43f5-bdbc-a374a5a8a38d", "status": "submitted", "start": "Scan 1", "end": "Scan 10"}
# curl 10.111.234.33:5000/jobs/all/
{
  "job.5afb2872-a428-43f5-bdbc-a374a5a8a38d": {
    "status": "complete",
    "id": "5afb2872-a428-43f5-bdbc-a374a5a8a38d"
  }
}
# curl '10.111.234.33:5000/jobs/id/?jobuuid=5afb2872-a428-43f5-bdbc-a374a5a8a38d'
{
  "image": "ready",
  "status": "complete",
  "end": "Scan 10",
  "x-y results": "passed",
  "id": "5afb2872-a428-43f5-bdbc-a374a5a8a38d",
  "start": "Scan 1"
}
# curl '10.111.234.33:5000/download/?jobuuid=5afb2872-a428-43f5-bdbc-a374a5a8a38d'
```
Now, you can move the out.png from the worker deployment into your local server using a command similar to this:
```bash
scp out.png tarinit@isp02.tacc.utexas.edu:/home/tarinit/
```
If you open the ```out.png``` the resulting png would look like:
![Glioblastoma Scatterplot](/final_project/plot_image/out.png)

If you would like to clear the job database, you can use the following code:
```bash
# curl 10.111.234.33:5000/jobs/delete/all/
All jobs were cleared.
```
### Redis
You can also check if the redis database is working correctly by doing the following:
```bash
$ kubectl exec -it redis-client-debug-deployment-5f88f47c96-mnzhj -- /bin/bash
# ipython
In [1]: import redis, json
In [2]: rd_job = redis.StrictRedis(host='10.104.122.228', port=6379, db=0)
In [3]: rd_data = redis.StrictRedis(host='10.104.122.228', port=6379, db=2)
In [4]: rd_data.keys()
Out[4]: [b'patients_key']
In [5]: json.loads(rd_data.get('patients_key').decode('utf-8'))
{outputs entire data dictionary}
In [6]: rd_job.keys()
Out[6]:
[b'job.e5669825-0958-44e9-85f8-d80222ac48b2',
 b'job.5afb2872-a428-43f5-bdbc-a374a5a8a38d']
```
