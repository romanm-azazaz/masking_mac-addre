import subprocess
import argparse
import uuid

class MacAddress:

    @classmethod
    def get_fake(cls):
        fake_mac_hec = uuid.uuid4().hex[6:12]
        default_mac_hec = hex(uuid.getnode()).replace('0x', '')[0:6]
        fake_mac = cls.formatting(default_mac_hec + fake_mac_hec)
        return fake_mac

    @classmethod
    def formatting(cls, mac_hex):
        mac = ':'.join(mac_hex[i: i + 2] for i in range(0, 11, 2))
        return mac

    @classmethod
    def spoofing(cls, interface, fake_mac):
        command_list = {'Darwin':f'ifconfig {interface} ether {fake_mac} \
                               && networksetup -setairportpower {interface} off \
                               && sleep 5 \
                               && networksetup -setairportpower {interface} on',
                        'Linux':f'ifconfig {interface} down \
                               && ifconfig {interface} hw ether {fake_mac} \
                               && ifconfig {interface} up'}
        command = command_list.get('Darwin')
        subprocess.call(command, shell=True)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', default='en0')
    script_arg = parser.parse_args()
    return script_arg

def main():
    script_arg = create_parser()
    fake_mac = MacAddress.get_fake()
    MacAddress.spoofing(script_arg.interface, fake_mac)

if __name__ == '__main__': 
    main()