import re

deviceConfig = open("config.txt", "r").read()

customerIpPattern = r'GigabitEthernet0/0.%s[ ]+([0-9\.]+)' % ('100')
customerIpAddress = re.search(customerIpPattern, deviceConfig)
print(customerIpAddress.group(1))

# Test