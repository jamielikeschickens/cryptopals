from challenge_3 import *

if __name__ == "__main__":
    cipher_text_file = open("4.txt")
    best_guesses = [brute_xor(line.strip('\n')) for line in cipher_text_file]

    best_guess = (0, '')
    for guess in best_guesses:
        if guess[0] > best_guess[0]:
            best_guess = guess
        
    print best_guess[1].strip("\n")

