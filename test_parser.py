import re


class ConfigurationParser:
    deviceConfig = open("config.txt", "r").read()
    def parseCustomerNames(self):
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        return customerNames

    def parseCustomerVlan(self, customerName):
        intPattern = (
                r"interface GigabitEthernet0/0.([0-9]+)\n  encapsulation "
                r"dot1Q [0-9]+\n  ip vrf forwarding %s"
                % 'CUSTOMER_A'
        )
        allCustomerSubInterfaces = re.search(intPattern, self.deviceConfig)
        return int(allCustomerSubInterfaces.group(1))

    def parseCustomerIPAddress(self, vlan):
        customerIpPattern = r'GigabitEthernet0/0.%s[ ]+([0-9\.]+)' % (vlan)
        customerIpAddress = re.search(customerIpPattern, self.deviceConfig)
        return customerIpAddress.group(1)
