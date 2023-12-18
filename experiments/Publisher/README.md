# project680
---

# Setting Up Kafka and Running Publisher-Subscriber



## Step 1: Download and Extract Kafka

1. Download Kafka from the official website: [https://kafka.apache.org/downloads](https://kafka.apache.org/downloads)

2. Extract the downloaded archive.
#change the config properties
3. advertised.listeners=PLAINTEXT://127.0.0.1:9092 // anyone can change this 

## Step 2: Start Zookeeper

1. Open a terminal and navigate to the Kafka directory.

2. Start Zookeeper with the following command:

./bin/zookeeper-server-start.sh config/zookeeper.properties


 keep the Zookeeper running and open a new terminal window

## Step 3: Start Kafka Server
1. Navigate to the Kafka directory and Start the Kafka server with the following command:

./bin/kafka-server-start.sh config/server.properties


## Step 4: Create a Kafka Topic
1. Open a new terminal window.

2. Navigate to the Kafka directory and Create a Kafka topic named "OTA" using the following command:
./bin/kafka-topics.sh --create --topic OTA --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

 
 ## Step 5: Python Environment Setup
=======


python3 -m venv myenv
source myenv/bin/activate   
pip install confluent-kafka


## Step 6: Configure Producer and Consumer
Edit the config.py file to set up Kafka configurations for both the producer and consumer scripts. Ensure the Kafka broker IP and the topic name are correct. I used 127.0.0 as I tested on my local machine 
=======
##Step 5: Run the Publisher
1. In a new terminal window, navigate to the directory containing your Python files.
python3 Publisher.py --input_file path/to/file


## Step 7: Run the Publisher
1. In a new terminal window, navigate to the directory containing your Python files. ( change the path up to the file you want to send)
python3 publisher.py --input_file /path/to/file   

## Step 8: Run the Subscriber
1. In a separate terminal window, navigate to the directory containing your Python files.
python3 Subscriber.py

