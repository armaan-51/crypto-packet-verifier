 

A client-server application written in Python to demonstrate cryptographic anti-spoofing and packet integrity verification using HMAC SHA256.

This was created for a 7th-semester cryptography assignment

#How to Run

1.  Clone the repository or download the files.
2.  Open two terminals.
3.  In the first terminal, start the server:
    ```
    python server.py
    ```
4.  In the second terminal, run the client:
    ```
    python client.py
    ```
The server will print a message indicating whether the received packet is valid and authentic.

## Technologies Used
- Python 3
- `socket` module for networking
- `hmac` and `hashlib` modules for cryptography
