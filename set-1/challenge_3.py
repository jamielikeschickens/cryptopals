from challenge_2 import fixed_xor 

def brute_xor(ciphertext):
    cipher_len = len(ciphertext)
    best_guess = (0, "")

    for key in range(0, 255):
        long_key =  str(key) * cipher_len

        result = fixed_xor(bytearray.fromhex(ciphertext), bytearray.fromhex(long_key))
        hex_string = ''.join(["%02x" % a for a in result])
        plaintext = hex_string.decode("hex")
        score = score_text(plaintext)

        if (score > best_guess[0]):
            best_guess = (score, plaintext)

    return best_guess

# A /very very/ simple scoring that could be made a lot more complex but at this stage
# what is the point? There's got to be a nicer way than this huge if statement too
def score_text(plaintext):
    score = 0
    for c in plaintext.lower():
        if (c == 'e' or c == 't' or c == 'a' or c == 'o' or c == 'i' or c == 'n'
                or c == 's' or c == 'h' or c == 'r' or c == 'd' or c== 'l' or c == 'u'
                or c == ' '):
            score += 1

    return score

if __name__ == "__main__":
    code = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print brute_xor(code)[1]

