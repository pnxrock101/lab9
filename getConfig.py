from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from getpass import getpass
import datetime

user = input('Please enter SSH username: ')
secret = getpass('Please enter SSH password: ')
date = datetime.date.today()

ciscoDevice = {
        'device_type': 'cisco_ios',
        'host': '192.168.108.129',
        'username': user,
        'password': secret
}

try:
    connection = ConnectHandler(**ciscoDevice)
    output = connection.send_command("show run")
    print(output, file=open("%s.txt" % date, "a+"))
except (NetMikoTimeoutException):
    print('The following device timed out: ' + ciscoDevice['host'])
except (AuthenticationException):
    print('Authentication failure on: ' + ciscoDevice['host'])
except (SSHException):
    print('Could not connect to the device with SSH.  Check your SSH settings on: ' + ciscoDevice['host'])
except (EOFError):
    print('End of file while attempting: ' + ciscoDevice['host'])
except Exception as other_error:
    print('The error ' + str(other_error) + ' occured while connecting to: ' + ciscoDevice['host'])
print('The script has completed')
