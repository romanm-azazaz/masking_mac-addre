import subprocess
import argparse
import uuid
import sys

class mac_address:

    @classmethod
    def get_default(cls):
        default_mac = cls.formatting_mac(hex(uuid.getnode()).replace('0x', ''))
        return default_mac

    @classmethod
    def get_fake(cls):
        fake_mac = cls.formatting_mac(uuid.uuid4().hex[0:12])
        return fake_mac

    @classmethod
    def formatting_mac(cls, mac_hex):
       mac = ':'.join(mac_hex[i: i + 2] for i in range(0, 11, 2))
       return mac

    @classmethod
    def call_switch(cls):
        interface = 'en0'
        print(F'default mac {cls.get_default()}\nfake mac {cls.get_fake()}')
        cmd = F'ifconfig {interface} ether {cls.get_fake()}'        
        print(cmd)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--random', action='store_const', const=True, default=False,
                        help='Generates a random set of characters similar to mac-faddres')
    script_key = parser.parse_args()
    return script_key.random

def main():
    if create_parser(): 
        mac_address.call_switch()
    else: sys.exit(1)

if __name__ == '__main__': main()

