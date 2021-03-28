# Tarini Thiagarajan's Exam 01 Description

The purpose of this project is to build upon previous homeworks regarding Dr. Moreau's island of animals. 

## Installation

Install this project by cloning the repository. Change directory to access the files. For example:

```bash
git clone https://github.com/tarinit2000/tt25926_coe332.git
cd tt25926_coe332/
cd exam01/
```

## Docker Compose

You can define and run a multi-container Docker application. Use the command:

```bash
docker-compose -p tarinithiagarajan-exam01 up -d
```

You can do the following curl statements:

```bash
curl localhost:5032/reset/

curl localhost:5032/animals/avglegs/

curl localhost:5032/animals/totalcount/

curl 'localhost:5032/animals/dates/?start_date=2021-03-24%2015:38:18.242800&end_date=2021-03-24%2015:38:18.243061'

curl 'localhost:5032/animals/uid/?uid=7638240a-ea9c-41bb-b796-83ce112145ca'

curl 'localhost:5032/animals/uidedit/?uid=7638240a-ea9c-41bb-b796-83ce112145ca&head=lion&body=rat-bat&arms=8&legs=3&tail=11&date=2021-03-24%2015:38:18.242900&uid_new=7638240a-ea9c-41bb-b796-83ce112145'  

curl 'localhost:5032/animals/delete/?start_date=2021-03-24%2015:38:18.242800&end_date=2021-03-24%2015:38:18.243061'
```
