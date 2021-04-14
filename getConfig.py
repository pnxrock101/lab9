from netmiko import ConnectHandler
from getpass import getpass

username = input('Please enter SSH username: ')
secret = getpass('Please enter SSH password: ')

ciscoDevice = {
        'device_type': 'cisco_ios',
        'host': '192.168.108.129',
        'username': user,
        'password': secret
}

connection = ConnectHandler(**ciscoDevice)
