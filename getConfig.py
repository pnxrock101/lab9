from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from getpass import getpass

user = input('Please enter SSH username: ')
secret = getpass('Please enter SSH password: ')

ciscoDevice = {
        'device_type': 'cisco_ios',
        'host': '192.168.108.129',
        'username': user,
        'password': secret
}

try:
    connection = ConnectHandler(**ciscoDevice)
except (NetMikoTimeoutException):
    print('The following device timed out: ' + ciscoDevice['host'])

print('The script has completed')
