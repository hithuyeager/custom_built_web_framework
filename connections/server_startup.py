import socket

from tiny_http.http_framing import Framing
from tiny_http.http_parser import parser
from tiny_http.responses import Responses,raw_response

HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 100


def main():
    no_of_responses = 0

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    connection = None

    try:
        while True:

            connection, address = server.accept()

            print(f"Connected: {address}")

            framing = Framing()

            while True:

                chunk = connection.recv(BUFFER_SIZE)

                if chunk == b"":
                    break

                print(f"Received {len(chunk)} bytes")

                complete_request = framing.new_bytes(chunk)

                if complete_request is not None:

                    request = parser(
                        complete_request.decode("utf-8")
                    )

                    print("\n--- COMPLETE REQUEST ---")
                    print("response no:",no_of_responses)
                    no_of_responses+=1
                    print(request)
                    obj = Responses()
                    connection.sendall(raw_response(obj))
                    break

    except Exception as error:

        print(f"Server error: {error}")

    finally:

        if connection is not None:
            connection.close()

        server.close()

        print("Server closed")


if __name__ == "__main__":
    main()