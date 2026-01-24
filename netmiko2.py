from netmiko import ConnectHandler

R1= "192.168.111.24"
R2= "192.168.111.23"
R3= "192.168.111.25"

Router_List = [R1, R2, R3]

for interfaces in Router_List:
    router_details = {
        "ip": interfaces,
        "username": "cisco",
        "password": "cisco",
        "device_type": "cisco_ios",
    }
    ssh = ConnectHandler(**router_details)
    print(interfaces + "connected successfully" )


    with open('configuration.txt') as file:
        content = file.read().splitlines()

    int_conf = ssh.send_config_set(content)

    int_details = ssh.send_command("show ip interface brief")
    print(int_details)
    user_choice = input("Enter command you would like to run to verify: ")
    user_choice=user_choice.lower()
    verification = ssh.send_command(user_choice)
    print(verification)
    ssh.save_config()
    ssh.disconnect()







