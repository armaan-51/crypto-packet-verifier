# server.py

import socket
import hmac
import hashlib

# --- Configuration ---
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
SECRET_KEY = b'my-super-secret-key' # The same pre-shared secret key

# --- Start Listening ---
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        
        # --- Receive and Process Packet ---
        packet = conn.recv(1024)
        if not packet:
            print("No data received. Closing connection.")
        else:
            print("\nReceived raw packet.")

            # 3. Parse the packet to separate data and the received tag
            try:
                message_data, received_mac_tag = packet.rsplit(b'|', 1)
            except ValueError:
                print("Packet format error. Could not split message and MAC.")
                exit()
                
            # 4. Calculate the expected MAC on the message data part
            expected_mac = hmac.new(SECRET_KEY, message_data, hashlib.sha256)
            expected_mac_tag = expected_mac.digest() # Get the MAC in bytes

            # 5. Securely compare the received tag with the expected tag
            #    We decode the received hex tag back to bytes for comparison.
            try:
                received_mac_bytes = bytes.fromhex(received_mac_tag.decode('utf-8'))
                is_valid = hmac.compare_digest(expected_mac_tag, received_mac_bytes)
            except (ValueError, UnicodeDecodeError):
                is_valid = False

            print(f"Received Message: {message_data.decode()}")
            print(f"Received HMAC Tag: {received_mac_tag.decode()}")
            print(f"Verification Result: {'VALID (Authentic)' if is_valid else 'INVALID (Spoofed or Tampered)'}")