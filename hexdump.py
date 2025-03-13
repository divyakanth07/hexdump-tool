import hexdump

def custom_hexdump(data: bytes, output_file):
    def to_printable_ascii(byte):
        return chr(byte) if 32 <= byte <= 126 else "."

    offset = 0
    with open(output_file, 'w') as ofile:
        while offset < len(data):
            chunk = data[offset : offset + 16]
            hex_values = " ".join(f"{byte:02x}" for byte in chunk)
            ascii_values = "".join(to_printable_ascii(byte) for byte in chunk)
            ofile.write(f"{offset:08x}  {hex_values:<48}  |{ascii_values}|\n")
            offset += 16


file_path = input('Enter the file path: ')
output_file = 'dump.txt'

if file_path == '0':
    data = b''
    for i in range(256):
        data += i.to_bytes(1, 'big')
    custom_hexdump(data, output_file)
else:
    with open(file_path, 'rb') as file:
        data = file.read()
    custom_hexdump(data, output_file)