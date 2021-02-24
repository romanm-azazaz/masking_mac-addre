import subprocess
import argparse
import uuid
import sys
import time

class mac_address:

    @classmethod
    def get_default(cls, platform):
        mac_hex = hex(uuid.getnode()).replace('0x', '')
        default_mac = cls.formatting_mac(mac_hex, platform)
        return default_mac

    @classmethod
    def get_fake(cls):
        mac_hex = uuid.uuid4().hex[0:12]
        fake_mac = cls.formatting_mac(mac_hex)
        return fake_mac

    @classmethod
    def formatting_mac(cls, mac_hex, platform=''):
        if not platform in 'linux': pass
        else: mac_hex = F'0{mac_hex}'
        mac = ':'.join(mac_hex[i: i + 2] for i in range(0, 11, 2))
        return mac

    @classmethod
    def call_switch(cls, interface, platform):
        fake_mac = cls.get_fake()
        print(F'default mac {cls.get_default(platform)}\nfake mac {fake_mac}')
        command_list = {'macos':F'ifconfig {interface} ether {fake_mac} &&\
                                  networksetup -setairportpower {interface} off &&\
                       sleep 5 && networksetup -setairportpower {interface} on',
                        'linux':F'ifconfig {interface} down &&\
                                  ifconfig {interface} hw ether {fake_mac} &&\
                                  ifconfig {interface} up'}
        command = command_list.get(platform)
        subprocess.call(command, shell=True)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-R', action='store_const', const=True, default=False,
                        help='Generates a random set of characters similar to mac-faddres')
    parser.add_argument('-i', '--interface')
    parser.add_argument('-p', '--platform', choices=['macos', 'linux'], default='macos')  
    script_key = parser.parse_args()
    return script_key

def main():
    script_key = create_parser()
    if script_key.R: mac_address.call_switch(script_key.interface, script_key.platform)
    else: sys.exit(1)

if __name__ == '__main__': main()

