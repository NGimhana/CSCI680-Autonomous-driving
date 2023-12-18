# Author:  Aljawharah Almuhana

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5560")

try:
    while True:
        with open('send_file.txt', 'rb') as f:
            data = f.read()
            print(data)
            try:
                socket.send(data)
                print("Message sent successfully")
            except zmq.error.ZMQError as e:
                print(f"Error sending message: {e}")
except KeyboardInterrupt:
    pass
finally:
    socket.close()
    context.term()
