#!/usr/bin/env python
#SMB-NULL-SCANNER

import argparse
import os
import subprocess

def parse_args():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Scan for SMB null sessions')
    parser.add_argument('--range', '-r', required=True, help='IP range to scan (e.g. 192.168.1.0/24)')
    return parser.parse_args()

def main():
    # Get command-line arguments
    args = parse_args()
    ip_range = args.range

    # Check if nbtscan is installed
    if not os.path.exists('/usr/bin/nbtscan'):
        print('Error: nbtscan is not installed. Please install nbtscan and try again.')
        return

    # Scan for null sessions using nbtscan
    cmd = 'nbtscan {}'.format(ip_range)
    try:
        output = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print('Error: nbtscan returned a non-zero exit status: {}'.format(e.returncode))
        return

    # Print null sessions
    lines = output.split('\n')
    for line in lines:
        if '<00>' in line:
            print(line)

if __name__ == '__main__':
    main()
