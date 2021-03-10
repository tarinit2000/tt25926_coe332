# Tarini Thiagarajan's Homework 03 Description

The purpose of this project is to build upon homeworks 01 and 02. For homework 03, I added an animal_consumer.py file that 
utilizes the python requests library. Also, I added a dockerfile, requirements.txt, and app.py. The app.py simply uses Flask 
and routes to my island animal JSON data. 

## Installation

Install this project by cloning the repository. Change directory to access the files. For example:

```bash
git clone https://github.com/tarinit2000/tt25926_coe332.git
cd tt25926_coe332/
cd homework03/web
```

## Running the Code

This code has three functions: 

1) To create a flask server that connects to a flask port:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -h localhost -p <your port number>
```
In a different window as flask runs: 

```bash
curl localhost:5032/animals/head/?name='snake'
curl localhost:5032/animals
curl localhost:5032/animals/legs/?number=6
```
Note: Do not ctrl-c out of the Flask server until you finish step 2.

2) To allow others to "consume" the data:

```bash
python3 animal_consumer.py
```

3) To containerize the Flask App:

```bash
docker build -t flask-helloworld-tarini:latest .
docker run --name "tarini-homework03" -d -p <your portnumber>:5000 flask-helloworld-tarini
docker ps -a
curl localhost:5032/animals/head/?name='snake'
curl localhost:5032/animals
curl localhost:5032/animals/legs/?number=6
```
