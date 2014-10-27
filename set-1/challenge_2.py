def fixed_xor(value_1, value_2):
    value_1 = bytearray.fromhex(value_1)
    value_2 = bytearray.fromhex(value_2)
    xored = [a ^ b for a, b in zip(value_1, value_2)]
    return xored

if __name__ == "__main__":
    xor_data = fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    xor_string = ""
    for x in xor_data:
        xor_string += ("%x" % x)

    print xor_string
