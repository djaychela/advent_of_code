"""Object-based version.  Took a couple of hours, but still couldn't get recursion working properly.
Gave up after taking a break"""

from dataclasses import dataclass, field
from data_read import read_file


bits = read_file("16_test.txt")

@dataclass
class Literal:
    version: int 
    id: int 
    packet: str 
    literal_value: int = 0
    leftover_bits: str = ""

    def __post_init__(self):
        self.read_literal_value()

    def read_literal_value(self):
        idx = 0
        done = False
        number = ""
        while not done:
            current_value = self.packet[idx:idx+5]
            number += current_value[1:]
            if current_value[0] == "0":
                done = True
            idx += 5
        self.literal_value = int(number, 2)
        self.leftover_bits = self.packet[idx:]
        # print(f"Literal RNS returns: {int(number, 2), self.packet[idx:], idx}")

@dataclass
class Operator:
    version: int
    id: int
    packet: str
    length_type: int = 0
    literal_value: int = 0
    sub_packets: list = field(default_factory=list)

    def __post_init__(self):
        self.parse_packet()

    def parse_packet(self):
        match self.id:
            case 4:
                print("ID 4: Number")
                number = Literal()
                number.load_data_binary(self.packet)
                print(f"{self.packet=}")
                print(number)
                self.read_number_string()
                number.read_number_string()
            case _:
                print(f"ID: {self.id}")
                if self.length_type == 0:
                    # 15 bit number for number of bits follows
                    sub_length = int(self.packet[1:16], 2)
                    print(f"{sub_length = } bits")
                    packet_data = self.packet[16:][:sub_length]
                    remains = self.packet[16:][sub_length:]
                    print(f"{packet_data=}")
                    print(f"{remains=}")
                    # decode packet data
                    
                    # while idx < sub_length + 22:
                    #     value, current_packet, val_length  = decode_packet(current_packet)
                    #     # print(f"{sub_length=} -> {value=}, {current_packet=}, {val_length=}")
                    #     idx += val_length
                    # packet_string = packet_string[idx:]
                else:
                    # 11 bit number for number of packets
                    sub_packets = int(self.packet[1:12], 2)
                    print(f"{sub_packets =}")
                    packet_data = self.packet[12:]
                    # print(f"{packet_data=}")
                    # parse packet data
                    while sub_packets > 0:
                        parse_packet(packet_data)
                        print(f"{sub_packets=}")
                        version, id, packet, length_type = parse_loaded_data(packet_data)
                        current_bits = Literal(version, id, packet)
                        self.sub_packets.append(current_bits)
                        packet_data = current_bits.leftover_bits
                        sub_packets -= 1
                    # packet_string = current_packet


def hex_convert_to_bin(input):
    return "".join([str(bin(int(bit, 16))[2:].zfill(4)) for bit in input.strip()])

def parse_loaded_data(binary):
    version = int(binary[:3], 2)
    id = int(binary[3:6], 2)
    packet = binary[6:]
    length_type = int(binary[6])
    return version, id, packet, length_type

def parse_packet(binary):
    version, id, packet, length_type = parse_loaded_data(binary_bits)
    if id == 4:
        return Literal(version, id, packet)
    else:
        return Operator(version, id, packet, length_type)

results = []
for bit in bits:
    print(bit)
    binary_bits = hex_convert_to_bin(bit)
    print(parse_packet(binary_bits))
    
