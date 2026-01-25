from netmiko import ConnectHandler


Router_List = open("routers.txt", "r")

for interfaces in Router_List:
    router_details = {
        "ip": interfaces,
        "username": "cisco",
        "password": "cisco",
        "device_type": "cisco_ios",
    }
    ssh = ConnectHandler(**router_details)
    print(interfaces + "connected successfully")

    with open('configuration.txt') as file:
        content = file.read().splitlines()
        int_conf = ssh.send_config_set(content)


#    output_file = open('pcheck_output.txt', 'a')
    output_file = open(r'C:\Users\dhruv\PycharmProjects\Python_dhruv_01\{}'.format(
        input("Enter the name of the file that you want to save data in: ")), 'a')

    with open('prechecks.txt') as file:
        verif_commands = file.read().splitlines()
        for command in verif_commands:
            verification = ssh.send_command(command)
            print(f"Output of '{command}':\n{verification}\n")
            output_file.write("\nThe below information is fetched from " + interfaces)
            output_file.write("\n" + verification + "\n")
    output_file.close()
    ssh.save_config()
    ssh.disconnect()
    print("Output exported successfully....!")






