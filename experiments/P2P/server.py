import socket
import os
import threading

FILE_SIZE = 5000000

def handle_send(client_socket):
        file_path = input("Enter the file path: ")
        try:
            file_name = os.path.basename(file_path)
            client_socket.send(file_name.encode())  # Send the file name
            with open(file_path, 'rb') as file:
                data = file.read(FILE_SIZE)
                while data:
                    client_socket.send(data)
                    data = file.read(FILE_SIZE)
            print("File sent.") 
                  
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        client_socket.close() 
    

def handle_receive(client_socket):
    received_data = b""
    file_name = client_socket.recv(FILE_SIZE).decode()  # Receive the file name
    while True:
        data = client_socket.recv(FILE_SIZE)
        if not data:
            break
        received_data += data

    if received_data:
        with open(file_name, 'wb') as file:
            file.write(received_data)
        print("File received.")

    client_socket.close()    

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('128.239.113.31', 12363))  # Change the port as needed
    server_socket.listen(5)
    print("Server started. Listening on port 12348.")

    while True:
        client_socket, addr = server_socket.accept()
        print("Got a connection from {}".format(addr))
        ## get the file path from the console

        send_handler = threading.Thread(target=handle_send, args=(client_socket,))
        send_handler.start()   
        

if __name__ == "__main__":
    start_server()
    
    
