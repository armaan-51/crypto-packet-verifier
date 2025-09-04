# client.py
import socket
import hmac
import hashlib

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
SECRET_KEY = b'my-super-secret-key' # The pre-shared secret key (as bytes)

# --- Create the Message and MAC ---
message = b"Hello, this is a legitimate packet!"

# 1. Create an HMAC object with the secret key and a hash algorithm
mac = hmac.new(SECRET_KEY, message, hashlib.sha256)

# 2. Get the hexadecimal representation of the MAC
mac_tag = mac.hexdigest()

print(f"Original Message: {message.decode()}")
print(f"Generated HMAC Tag: {mac_tag}")

# 3. Prepare the packet: message + delimiter + mac_tag
#    We encode to bytes for sending over the network.
packet = message + b'|' + mac_tag.encode('utf-8')

# --- Send the Packet ---
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("\nConnecting to server...")
    s.connect((HOST, PORT))
    print("Sending packet...")
    s.sendall(packet)
    print("Packet sent successfully.")