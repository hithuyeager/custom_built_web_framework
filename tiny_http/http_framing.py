class Framing:

    def __init__(self):
        self.buffer = b""

    def new_bytes(self, raw_bytes: bytes):

        if raw_bytes == b"":
            return None

        self.buffer += raw_bytes

        # We don't have the complete headers yet.
        if b"\r\n\r\n" not in self.buffer:
            return None

        header_bytes, remaining = self.buffer.split(
            b"\r\n\r\n",
            1
        )

        headers = header_bytes.split(b"\r\n")

        content_length = 0

        for line in headers[1:]:

            key, value = line.split(b":", 1)

            if key.lower() == b"content-length":
                content_length = int(value.strip())

        # We have not received the complete body yet.
        if len(remaining) < content_length:
            return None

        # Complete HTTP request.
        request_bytes = (
            header_bytes
            + b"\r\n\r\n"
            + remaining[:content_length]
        )

        # Preserve bytes belonging to a possible next request.
        self.buffer = remaining[content_length:]

        return request_bytes