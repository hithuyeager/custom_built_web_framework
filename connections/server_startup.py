import json
import socket


HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    connection = None

    try:
        connection, address = server.accept()
        print(f"Connected: {address}")

        while True:
            raw_data = connection.recv(BUFFER_SIZE)

            if not raw_data:
                print("Client disconnected")
                break

            data = json.loads(raw_data.decode())

            if data["type"] == "system":
                if data["action"] == "shutdown":
                    print("Shutdown requested")
                    break

            elif data["type"] == "user":
                print("Client:", data["data"])

                response = {
                    "data": "received"
                }

                connection.sendall(
                    json.dumps(response).encode()
                )

    except Exception as error:
        print(f"Server error: {error}")

    finally:
        if connection is not None:
            connection.close()

        server.close()
        print("Server closed")


if __name__ == "__main__":
    main()