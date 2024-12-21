def to_decimal(mask):
    
    res = []
    binary_mask = bin(mask)[2:]

    padded_binary_mask = binary_mask.zfill(((len(binary_mask) + 7) // 8) * 8)
   
    for i in range(0, len(padded_binary_mask), 8):
        res.append(int(padded_binary_mask[i:i+8], 2))

    return res



def main():
    
    address = '165.245.12.88' #input("Enter the address: ")
    print(f"address: {address}")

    parts = address.split('.')
    full = bin((int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3]))
    print(f"the address in binary: {full}")

    cidr = 24 #int(input("Enter the CIDR: "))
    print(f"cidr: {cidr}")
    mask = (4294967295 >> (32-cidr))<<(32-cidr)
    decimal_subnet = to_decimal(mask)
    
    subnet_mask = ".".join(map(str,decimal_subnet))
    print(f"subnet mask: {subnet_mask}")


    subnet_id = int(full, 2) & mask
    decimal_subnet_id = to_decimal(subnet_id)
    subnet_id_formatted = ".".join(map(str,decimal_subnet_id))
    print(f"subnet id: {subnet_id_formatted}")

    wildcard = ~mask & 0xFFFFFFFF
    broadcast_address = subnet_id | wildcard
    decimal_broadcast = to_decimal(broadcast_address)
    broadcast_formatted = ".".join(map(str,decimal_broadcast))
    print(f"broadcast address: {broadcast_formatted}")

    first_host = decimal_subnet_id
    first_host[3] += 1
    first_host_formatted = ".".join(map(str,first_host))
    print(f"first host: {first_host_formatted}")

    last_host = decimal_broadcast
    last_host[3] -= 1
    last_host_formatted = ".".join(map(str,last_host))
    print(f"last host: {last_host_formatted}")

    


if __name__ == "__main__":
    main()