import sys
import subprocess
import os 
from decouple import config

IP_NETWORK = config('IP_NETWORK_PAUL')
IP_DEVICE = config('IP_DEVICE_PAUL')

proc = subprocess.Popen(['ping', IP_NETWORK,'-b'], stdout=subprocess.PIPE)

while True:
        line = proc.stdout.readline()
        if not line:
                break
        connected_ip = line.decode('utf-8').split()[3]
        print(connected_ip[:-1])

        if connected_ip[:-1] == IP_DEVICE:
                subprocess.Popen(['spd-say', 'Buna ziua!'])
                exit(0)