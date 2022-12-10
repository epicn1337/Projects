# Creator: Paul Olushile(nix)
# A little advanced network scanner  uses the Scapy library to scan the target network and send custom packets to each active host to check for open ports.
# It sends a TCP packet with the SYN flag set to each port in the specified range and checks the response to determine if the port is open.

##NOTE: 
# Please note that this script only checks for open ports using the SYN/ACK flag, but it does not establish a full connection to the target host.
# To build a more comprehensive network scanner, you can add additional functionality, 
# such as analyzing the responses to identify the services running on each open port or performing vulnerability assessments.
 
from scapy.all import *

# Set the target IP address or hostname
target = '192.168.0.1/24'

# Set the timeout value (in seconds)
timeout = 2

# Set the minimum and maximum port numbers to scan
min_port = 1
max_port = 1024

# Scan the target network
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target), timeout=timeout)

# Print the results
for snd, rcv in ans:
    # Print the IP address and MAC address of the active host
    print("Host {} is up".format(rcv.sprintf(r"%ARP.psrc%")))
    print("MAC address: {}".format(rcv.sprintf(r"%Ether.src%")))

    # Scan the host for open ports
    for port in range(min_port, max_port+1):
        # Create a TCP packet with the SYN flag set
        pkt = IP(dst=rcv.sprintf(r"%ARP.psrc%"))/TCP(dport=port, flags="S")

        # Send the packet and receive the response
        response = sr1(pkt, timeout=timeout, verbose=0)

        # If the response is not None and the response has the SYN/ACK flag set,
        # the port is open
        if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            print("Port {} is open".format(port))
