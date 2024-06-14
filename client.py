import socket
import threading


host = input("Enter server (e.g., 127.0.0.1): ")
port = int(input("Enter port (e.g., 55555): "))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('utf-8'))

username = input("Enter your username: ")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
