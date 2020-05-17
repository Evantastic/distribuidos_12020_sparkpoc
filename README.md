# Apache Spark, a proof of concept
In order to make this work, `docker` and `docker-compose` must be installed.

The first step to make is to start up the containers
``` bash
docker-compose up
```
Then, to see it its working, check `localhost:8080` to see if the page of the master node is up and running.

We then have to enter the container of the master node
``` bash
docker exec -it spark-poc_master_1 /bin/bash
```
Lastly, we submit the script to count the words
``` bash
./bin/spark-submit --master spark://master:7077 /tmp/data/poc.py
```
The results will be written to `./data/resultado`
