#!/bin/bash

# This script scans for an active directory on a target network

# Store the target network in a variable
target_network="Ip-Range/24"

# Use nmap to scan the target network for active directory services
nmap -p 389 --open $target_network -oG - | grep "389/open/tcp" > ad_hosts.txt

# Print the list of hosts that are running active directory services
cat ad_hosts.txt | tee ad_scan.log

# Check if the scan was successful
if [ $? -eq 0 ]; then
  echo "Active directory scan was successful" | tee -a ad_scan.log
else
  echo "Active directory scan failed" | tee -a ad_scan.log
fi

# Check if any active directory hosts were found
if [ -s ad_hosts.txt ]; then
  echo "Found active directory hosts" | tee -a ad_scan.log
  # Use ldapsearch to query the active directory hosts
  while read host; do
    ldapsearch -h $host -x -b "dc=domain,dc=com" "(objectclass=*)" | tee -a ad_scan.log
  done < ad_hosts.txt
else
  echo "No active directory hosts were found" | tee -a ad_scan.log
fi
