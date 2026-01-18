import paramiko
import netmiko
from netmiko import ConnectHandler
from netmiko2 import commands



password = input ("Enter device password: ")

router_details = {
"ip":"192.168.111.23",
"username":"cisco",
"password": password,
"device_type":"cisco_ios",
}

ssh = ConnectHandler(**router_details)
print("Connection with Router X established sucessfully!")

with open('configuration.txt') as file:
    content = file.read().splitlines()


int_conf =  ssh.send_config_set(content)
print(int_conf)

int_details = ssh.send_command("show ip interface brief")
print(int_details)

ospf_config = ssh.send_command("show run | section router ospf")
print(ospf_config)

ssh.save_config()
ssh.disconnect()