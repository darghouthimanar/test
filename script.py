from netmiko import ConnectHandler
#informations de connexion
router = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": 22 
}

#connexion au router
conn = ConnectHandler(**router)
#afffiche l'heure
clock = conn.send_command("show clock")
print(clock)
#affichage les interfaces
interfac = conn.send_command("sh ip int br")
with open("interfaces.txt", "w") as file:
    file.write(interfac)
print('interfaces.txt')
#configuration interfaces loopback avec ip 
commands = [
    "interface loopback 8",
    "ip address 10.8.8.8 255.255.255.240",
    "no shutdown"
]
configuration = conn.send_config_set(commands)
print(configuration)

