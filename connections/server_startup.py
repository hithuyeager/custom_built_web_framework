import socket
from http.http_parser import parser


HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 100


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    connection = None

    try:
        connection, address = server.accept()
        print(f"Connected: {address}")

        raw_data = b""

        while True:
            chunk = connection.recv(BUFFER_SIZE)

            if chunk == b"":
                break

            print(f"Received {len(chunk)} bytes")
            raw_data += chunk

        parser(raw_data)

    except Exception as error:
        print(f"Server error: {error}")

    finally:
        if connection is not None:
            connection.close()

        server.close()
        print("Server closed")


if __name__ == "__main__":
    main()