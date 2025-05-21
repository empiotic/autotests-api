import socket

def main():
    # Первое подключение
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    message = "Привет, сервер!"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"{response}")

    client_socket.close()

    # Второе подключение
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    message = "Как дела?"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"{response}")

    client_socket.close()

if __name__ == '__main__':
    main()