def parser(raw_data):

    parts = raw_data.split("\r\n\r\n")

    header = parts[0].split("\r\n")

    first_line = header[0]
    request_line = first_line.split(" ")

    method = request_line[0]
    path = request_line[1]
    version = request_line[2]

    header_info = {}

    for i in range(1, len(header)):

        current_line = header[i]

        if current_line == "":
            break

        separator = current_line.find(":")

        key = current_line[:separator]
        value = current_line[separator + 1:].strip()

        header_info[key] = value

    body = parts[1] if len(parts) > 1 else ""

    return {
        "method": method,
        "path": path,
        "version": version,
        "headers": header_info,
        "body": body
    }