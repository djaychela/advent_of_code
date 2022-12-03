"""Minor revision of first version, still doesn't work"""


from data_read import read_file

bits = read_file("16_test_2.txt")

def hex_convert(input):
    return "".join([str(bin(int(bit, 16))[2:].zfill(4)) for bit in input.strip()])

def read_number_string(packet):
    idx = 6
    done = False
    number = ""
    while not done:
        current_value = packet[idx:idx+5]
        number += current_value[1:]
        if current_value[0] == "0":
            done = True
        idx += 5
    print(f"RNS returns: {int(number, 2), packet[idx:], idx}")
    return (int(number, 2), packet[idx:], idx)

def decode_packet(packet_string):
    global version_list

    # print(f"Starting: {packet_string = }")
    if packet_string == None:
        return
    if len(packet_string) <=7:
        return 0, "" , 100000000
    version = int(packet_string[:3], 2)
    id = int(packet_string[3:6], 2)
    version_list.append(version)
    print(f"{version=}, {id=}")
    match id:
        case 4:            
            return read_number_string(packet_string)
        case _:
            len_id = packet_string[6]
            if len_id == "0":
                sub_length = int(packet_string[7:22], 2)
                print(f"{sub_length = }")
                # slice string and pass to decode_packet repeatedly
                idx = 22
                current_packet = packet_string[22:]
                while idx < sub_length + 22:
                    value, current_packet, val_length  = decode_packet(current_packet)
                    # print(f"{sub_length=} -> {value=}, {current_packet=}, {val_length=}")
                    idx += val_length
                packet_string = packet_string[idx:]
            else:
                sub_packets = int(packet_string[7:18], 2)
                print(f"{sub_packets = }")
                current_packet = packet_string[18:]
                while sub_packets > 0:
                    value, current_packet, val_length  = decode_packet(current_packet)
                    # print(f"{sub_packets=}")
                    # print(f"{value=}, {current_packet=}, {val_length=}")
                    sub_packets -= 1
                packet_string = current_packet

    # print(f"{packet_string = }")
    # pause = input("Waiting...")
    return 0, packet_string, 0

results = []
for bit in bits:
    current = hex_convert(bit)
    version_list = []
    decode_packet(current)
    results.append(f"{bit.strip()} -> {sum(version_list)}")


for result in results:
    print(result)