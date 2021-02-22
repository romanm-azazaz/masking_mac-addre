import subprocess
import argparse
import random
import uuid

class mac_address:

    @staticmethod
    def get_defolt():
        defolt_mac = formatting_mac(hex(uuid.getnode()).replace('0x', ''))
        return defolt_mac

    @staticmethod
    def generation():
        substitute_mac = formatting_mac(uuid.uuid4().hex[0:12])
        return substitute_mac

    @staticmethod
    def switch():
        cmd = F'ifconfig #{interface} ether #{mac_address}'

def formatting_mac(mac_hex):
       mac = ':'.join(mac_hex[i: i + 2] for i in range(0, 11, 2))
       return mac

defolt_mac = mac_address.get_defolt()
substitute_mac = mac_address.generation()

print(F'defolt_mac {DEFOLT_MAC}\nsubstitute_mac {substitute_mac}')