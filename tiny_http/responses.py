class Responses:
    def __init__(self):
        self.status_code = 200
        self.message = "success"
    def server_error(self):
        print("entered to error block")
        self.status_code = 500
        self.message = "internal server error"
def raw_response(obj: object):
    data = (
                f"HTTP/1.1 {obj.status_code} {obj.message}\r\n"
                f"Content-Type: text/plain\r\n"
                f"Content-Length: {len((obj.message).encode())}\r\n"
                f"\r\n"
                f"{obj.message}"
            )
    return data.encode("utf-8")

 