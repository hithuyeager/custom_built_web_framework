import socket


HOST = "127.0.0.1"
PORT = 5000


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to server")

    request = (
        "GET /hello HTTP/1.1\r\n"
        "Host: localhost:5000\r\n"
        "User-Agent: TinyClient/1.0\r\n"
        "Accept: text/plain\r\n"
        "\r\n"
    )

    client.sendall(request.encode("utf-8"))

    data = client.recv(1000)

    print(data.decode("utf-8"))
    

    client.close()


if __name__ == "__main__":
    for i in range(10000):
        main()