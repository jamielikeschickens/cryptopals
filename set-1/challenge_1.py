import sys

if __name__ == "__main__":
    hex_bytes = bytearray.fromhex(sys.argv[1])

# Most definitely a faster way to do this but I wanted to write it myself
# if anyone wants to run me through it that'd be great thanks

base_64_table = ascii.uppercase + ascii.lowercase + "+/"

def hex_to_base64(byte_string):
    offset = 0
    byte_str_length = len(byte_string)
    conv_array = bytearray()

    pad_bytes = 3 - (byte_str_length % 3)
    if (pad_bytes == 3):
        pad_bytes = 0

    for i in xrange(pad_bytes):
        print "padded"
        byte_string.append(0x00)

    while (byte_str_length > 0):
        index = ((byte_string[0 + offset] & 0xFC) >> 2)
        conv_array.append(base_64_table[index])

        index = ((((byte_string[0 + offset] & 0x03) << 4) | 
            ((byte_string[1 + offset] & 0xF0) >> 4)))

        conv_array.append(base_64_table[index])

        index = (((byte_string[1 + offset] & 0x0F) << 2) | 
                ((byte_string[2 + offset] & 0xC0) >> 6))
        conv_array.append(base_64_table[index])

        index = (byte_string[2 + offset] & 0x3F)
        conv_array.append(base_64_table[index])

        offset += 3
        byte_str_length -= 3

    for i in xrange(pad_bytes):
        conv_array.append('=')

    return conv_array
