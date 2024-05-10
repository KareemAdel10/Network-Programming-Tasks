from socket import *

try:
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 7002  # The port used by the server

    HEADER_LENGTH = 4  # Assuming 4 bytes for message length

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        message = input("client: ")
        message_length = len(message.encode('utf-8'))

        # Send message length
        s.sendall(message_length.to_bytes(HEADER_LENGTH, byteorder="big"))

        # Send message data
        s.sendall(message.encode('utf-8'))

        # Receive response (optional)
        response_length = int.from_bytes(s.recv(HEADER_LENGTH), byteorder="big")
        response_data = s.recv(response_length)
        print("server:", response_data.decode('utf-8'))

except error as e:
    print(e)

except KeyboardInterrupt:
    print("chat is terminated")