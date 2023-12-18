# Author: Nadeeshan De Silva

import socket
import threading
import os
import time

FILE_SIZE=5000000

def send_file(server_ip, server_port):
    file_path = input("Enter the file path: ")

    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender_socket.connect((server_ip, server_port))
    file_name = os.path.basename(file_path)

    try:
        sender_socket.send(file_name.encode())  # Send the file name
        with open(file_path, 'rb') as file:
            data = file.read(FILE_SIZE)
            while data:
                sender_socket.send(data)
                data = file.read(FILE_SIZE)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    sender_socket.close()

def receive_file(server_ip, server_port):
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver_socket.connect((server_ip, server_port))

    while True:
        
        received_data = b""
        file_name = receiver_socket.recv(FILE_SIZE).decode()  # Receive the file name

        start_time = 0
        while True:
            data = receiver_socket.recv(FILE_SIZE)
            if not data:
                break
            else:
                if start_time == 0:
                    start_time = time.time()  
                received_data += data

        if received_data:
            with open(file_name, 'wb') as file:
                file.write(received_data)
            print(f"File received: {file_name}")
            end_time = time.time()
            print(f"Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    server_ip = '127.0.0.1'  # Replace with Peer A's IP address
    server_port = 12353

    # send_thread = threading.Thread(target=send_file, args=(server_ip, server_port))
    receive_thread = threading.Thread(target=receive_file, args=(server_ip, server_port))

    # send_thread.start()
    receive_thread.start()
