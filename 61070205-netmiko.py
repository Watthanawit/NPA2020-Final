from netmiko import ConnectHandler

device_ip = '10.0.15.114'
username = 'admin'
password = 'cisco'

device_params = {'device_type': 'cisco_ios',
             'ip': device_ip,
             'username': username,
             'password': password
            }
with ConnectHandler(**device_params) as ssh:
    config_commands = [
    'int loopback 61070205',
    'ip add 192.168.1.1 255.255.255.0',
    'no shut'
    ]
    sentConfig = ssh.send_config_set(config_commands)
