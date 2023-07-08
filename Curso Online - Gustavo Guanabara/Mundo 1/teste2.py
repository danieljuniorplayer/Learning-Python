import hashlib
import itertools


def create_ntlm_hash(value):
    return hashlib.new('md4', value.encode('utf-16le')).hexdigest()


def decode_ntlm_hash(ntlm_hash):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_length = 7

    # Testar com números
    for length in range(1, max_length + 1):
        for combination in itertools.product("0123456789", repeat=length):
            word = ''.join(combination)
            hash_attempt = create_ntlm_hash(word)

            print(f"Testando número: {word}, Hash: {hash_attempt}")

            if hash_attempt == ntlm_hash:
                return word

    # Testar com palavras
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            word = ''.join(combination)
            hash_attempt = create_ntlm_hash(word)

            print(f"Testando palavra: {word}, Hash: {hash_attempt}")

            if hash_attempt == ntlm_hash:
                return word

    return None


# Pedir a hash NTLM para decodificar
ntlm_hash = input("Digite a hash NTLM: ")
ntlm_hash = ntlm_hash.lower()
# Decodificar a hash
decoded_word = decode_ntlm_hash(ntlm_hash)

if decoded_word:
    print("A palavra original é:", decoded_word)
else:
    print("Não foi possível decodificar a hash.")
