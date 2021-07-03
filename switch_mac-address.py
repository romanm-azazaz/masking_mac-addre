import subprocess
import argparse
import uuid

class MacAddress:

    @classmethod
    def get_default(cls):
        mac_hex = hex(uuid.getnode()).replace('0x', '')
        return mac_hex

    @classmethod
    def get_fake(cls):
        fake_mac_hec = uuid.uuid4().hex[0:12]
        default_mac_hec = cls.get_default()
        fake_mac = cls.formatting_mac(default_mac_hec[0:6] + fake_mac_hec[6:12])
        print(F'Generated fake mac {fake_mac}')
        return fake_mac

    @classmethod
    def formatting_mac(cls, mac_hex):
        mac = ':'.join(mac_hex[i: i + 2] for i in range(0, 11, 2))
        return mac

    @classmethod
    def call_switch(cls, interface):
        fake_mac = cls.get_fake()
        command_list = {'macos':F'ifconfig {interface} ether {fake_mac} &&\
                                  networksetup -setairportpower {interface} off &&\
                       sleep 5 && networksetup -setairportpower {interface} on'}
        command = command_list.get('macos')
        subprocess.call(command, shell=True)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', default='en0')
    script_arg = parser.parse_args()
    return script_arg

def main():
    script_arg = create_parser()
    MacAddress.call_switch(script_arg.interface)

if __name__ == '__main__': main()

