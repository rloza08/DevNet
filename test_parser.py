import re


class ConfigurationParser:
    deviceConfig = open("config.txt", "r").read()
    def parseCustomerNames(self):
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        return customerNames

