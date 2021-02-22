import subprocess
import argparse
import random
import uuid

class mac_address:

    @classmethod
    def get_defolt(cls):
        defolt_mac = cls.formatting_mac(hex(uuid.getnode()).replace('0x', ''))
        return defolt_mac

    @classmethod
    def generation(cls):
        substitute_mac = cls.formatting_mac(uuid.uuid4().hex[0:12])
        return substitute_mac

    @classmethod
    def formatting_mac(cls, mac_hex):
       mac = ':'.join(mac_hex[i: i + 2] for i in range(0, 11, 2))
       return mac

    @classmethod
    def switch(cls):
        cmd = F'ifconfig #{interface} ether #{cls.generation}'


defolt_mac = mac_address.get_defolt()
substitute_mac = mac_address.generation()

print(F'defolt_mac {defolt_mac}\nsubstitute_mac {substitute_mac}')