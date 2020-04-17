import re

deviceConfig = open("config.txt", "r").read()
intPattern = (
    r"interface GigabitEthernet0/0.([0-9]+)\n  encapsulation "
    r"dot1Q [0-9]+\n  ip vrf forwarding %s"
    % 'CUSTOMER_A'
)

allCustomerSubInterfaces = re.search(intPattern, deviceConfig)

print(allCustomerSubInterfaces.group(1))
