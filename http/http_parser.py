def parser(bytes):
    raw_data = bytes.decode("utf-8")
    parts = raw_data.split("\r\n\r\n") 
    header = parts[0].split("\r\n")
    body = parts[1]
    first_line = header[0]
    header_info = {}
    for i in range(len(header)):
        if i == 0 :
            continue
        if header[i] == "":
            break
        current_line = header[i]
        key = current_line[:current_line.find(":")]
        value = current_line[current_line.find(":")+1:].strip()
        header_info[key] = value
    body_end = int(header_info['Content-Length'])
    body_content = body[:body_end]
    print(body_content)

    