from challenge_2 import fixed_xor

if __name__ == "__main__":
    key = "ICE"
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    
    long_key = ''
    i = 0

    # Probably a nicer way to do this look into it
    for plain_text in range(len(plaintext)):
        long_key += key[i % len(key)]
        i += 1

    xor_data = fixed_xor(bytearray(long_key), bytearray(plaintext))
    final_string = ''.join(["%02x" % x for x in xor_data])
    print final_string
        

