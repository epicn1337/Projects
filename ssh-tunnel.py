# Creator: Paul Olushile
# Basic SSH Tunnel

import os

# Host and port to forward the connection to
FORWARD_HOST = "localhost"
FORWARD_PORT = 8080

# Host and port to bind the tunnel to on the local machine
BIND_HOST = "localhost"
BIND_PORT = 8000

# SSH server host and port
SSH_HOST = "ssh.example.com"
SSH_PORT = 22

# SSH username and password
SSH_USERNAME = "sshuser"
SSH_PASSWORD = "sshpass"

# Create the SSH tunnel
os.system(f"sshpass -p {SSH_PASSWORD} ssh -L {BIND_HOST}:{BIND_PORT}:{FORWARD_HOST}:{FORWARD_PORT} {SSH_USERNAME}@{SSH_HOST} -p {SSH_PORT}")

## Adding colorama to the script:
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################

from colorama import Fore, Style

# Host and port to forward the connection to
FORWARD_HOST = "localhost"
FORWARD_PORT = 8080

# Host and port to bind the tunnel to on the local machine
BIND_HOST = "localhost"
BIND_PORT = 8000

# SSH server host and port
SSH_HOST = "ssh.example.com"
SSH_PORT = 22

# SSH username and password
SSH_USERNAME = "sshuser"
SSH_PASSWORD = "sshpass"

# Header with SSH Tunneling logo and colors
print(Fore.CYAN + Style.BRIGHT + "   _____ ____  ____ _____ _____ _   _ ____  _____ ")
print(Fore.CYAN + Style.BRIGHT + "  | ____|  _ \|  _ \_   _| ____| \ | |  _ \| ____|")
print(Fore.CYAN + Style.BRIGHT + "  |  _| | |_) | |_) || | |  _| |  \| | | | |  _|  ")
print(Fore.CYAN + Style.BRIGHT + "  | |___|  __/|  _ < | | | |___| |\  | |_| | |___ ")
print(Fore.CYAN + Style.BRIGHT + "  |_____|_|   |_| \_\|_| |_____|_| \_|____/|_____|")
print(Style.RESET_ALL)

# Create the SSH tunnel
os.system(f"sshpass -p {SSH_PASSWORD} ssh -L {BIND_HOST}:{BIND_PORT}:{FORWARD_HOST}:{FORWARD_PORT} {SSH_USERNAME}@{SSH_HOST} -p {SSH_PORT}")
