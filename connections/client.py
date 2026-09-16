import json
import socket


HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to server")

    try:
        while True:
            user_input = input(
                "Enter message (type 'stop' to close): "
            ).strip()

            if user_input.lower() == "stop":
                shutdown_message = {
                    "type": "system",
                    "action": "shutdown"
                }

                client.sendall(
                    json.dumps(shutdown_message).encode()
                )

                break

            message = {
                "type": "user",
                "data": user_input
            }

            client.sendall(
                json.dumps(message).encode()
            )

            raw_response = client.recv(BUFFER_SIZE)

            if not raw_response:
                print("Server disconnected")
                break

            response = json.loads(raw_response.decode())

            print("Server:", response)

    finally:
        client.close()
        print("Client closed")


if __name__ == "__main__":
    main()