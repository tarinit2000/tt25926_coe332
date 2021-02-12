# Tarini Thiagarajan's Homework 02 Description

The purpose of this project is to build upon homework 01. To recap from homework 01, I created a generate_animals.py 
that generates a JSON file of twenty assembled animals. I also created a read_animals.py that reads in and prints one animal at random.
For homework 02, I added a new "breed" feature to the read_animals.py script that breeds one child from two random but unique parents. 

## Installation

Install this project by cloning the repository. Change directory to access the files. For example:

```bash
git clone https://github.com/tarinit2000/tt25926_coe332.git
cd tt25926_coe332/
cd homework02/
```

## Running the Code

This code has two functions: 

1) To generate an animals.json file of twenty assembled animals: 

```bash
python3 generate_animals.py animals.json
cat animals.json
```

2) To read in animals.json, print one animal at random, and print a child of two random but distinct parent animals:

```bash
python3 read_animals.py animals.json
```

## Docker Image

You can build a Docker image using the provided Dockerfile. Use the commands:

```bash
git clone https://github.com/tarinit2000/tt25926_coe332.git
cd tt25926_coe332/
cd homework02/
docker build -t <dockerhubusername>/json-animal:1.0 .
```

An example of running the scripts inside a container is:

```bash
docker run --rm -it <dockerhubusername>/json-animal:1.0 /bin/bash
ls /code
cd /home
generate_animals.py test.json
read_animals.py test.json
```

An example of running the scripts non-interactively:

```bash
mkdir test
cd test
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) <dockerhubusername>/json-animal:1.0 generate_animals.py /data/animals.json
docker run --rm -v $PWD:/data <dockerhubusername>/json-animal:1.0 read_animals.py /data/animals.json
```

## Test

Test the breed feature of the read_amimals.py by running:

```bash
python3 test_read_animals.py
```
