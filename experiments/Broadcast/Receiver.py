# Author:  Aljawharah Almuhana

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
 
try:
    socket.connect("tcp://localhost:5560")
    print("Connected successfully!")
except zmq.error.ZMQError as e:
    print(f"Error connecting: {e}")

    
socket.setsockopt_string(zmq.SUBSCRIBE, "")

try:
    print("Testing")
    data = socket.recv()
except zmq.error.ZMQError as e:
    print(f"Error receiving message: {e}")
     
print("Received data:", data)

with open('received_file.txt', 'wb') as f:
    f.write(data)
    print("File saved successfully")
