import hashlib
import itertools
import time
import random
import string


def decode_ntlm_hash(ntlm_hash):
    characters = string.ascii_letters + string.digits
    max_length = 7

    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            word = ''.join(combination)
            hash_attempt = hashlib.new('md4', word.encode('utf-16le')).hexdigest()

            print(f"Testing word: {word}")

            if hash_attempt == ntlm_hash:
                return word

    return None


# Prompt for the NTLM hash to decode
ntlm_hash = input("Enter the NTLM hash: ")
ntlm_hash = ntlm_hash.lower()
# Decode the hash
decoded_word = decode_ntlm_hash(ntlm_hash)

if decoded_word:
    print("The original word is:", decoded_word)
else:
    print("Failed to decode the hash.")
