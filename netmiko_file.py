from netmiko import ConnectHandler

# Define the device to connect to
device = {
    'device_type': 'juniper_junos',
    'host': '10.5.5.45',  # IP address of the device
    'username': 'supun',
    'password': '#smm1123',
}

# Connect to the device
net_connect = ConnectHandler(**device)
prompt = net_connect.find_prompt()

# Configuration commands to set interface description
interface = 'ge-0/0/0'  # Example interface
description = 'Connected to Switch B'

config_commands = [
    f'set interfaces {interface} description "{description}"',
    'commit',  # Commit the configuration
    'exit',  # Exit configuration mode
]

# Send configuration to the device
output = net_connect.send_config_set(config_commands)

# Print the output (optional)
print(output)

# Disconnect from the device
net_connect.disconnect()
