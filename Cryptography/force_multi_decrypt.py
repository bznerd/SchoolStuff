import math
import enchant
LETTERS = "abcdefghijklmnopqrstuvwxyz"
COMMON_WORDS = ""
DICTIONARY = enchant.Dict('en_US')
CHAR_SET = 26

def get_english(string):
    return len([string[x:y] for x in range(len(string)) for y in range(x+3,len(string)+1) if DICTIONARY.check(string[x:y])])

def clean_input(input_string):
    return ''.join([char.lower() for char in input_string if char.lower() in LETTERS])
    
def multiplicative_cipher(text, key):
    return ''.join([LETTERS[int((LETTERS.find(char)*key)%26)] for char in text]).lower()

def find_primes_less_than(max):
    if max < 2: return []
    primes = [2]
    for x in range(3,max+1):
        for prime in primes:
            if prime > math.sqrt(x):
                primes.append(x)
                break
            if x%prime == 0: break
        
    return primes
        
def get_prime_factors(num):
    prime_factors = []
    for prime in find_primes_less_than(int((num/2)+1)):
        if num%prime == 0: prime_factors.append(prime)
    return prime_factors
        
def get_coprimes_less_than(num):
    numbers = range(1,num)
    for prime in get_prime_factors(num):
        numbers = [x for x in numbers if x not in range(prime,26,prime)]
    return numbers
        
def modular_multi_inverse(m, a, r=1):
    if r%a == 0: return r/a
    return int((m * modular_multi_inverse(a,(m%a),a-(r%a)))/a + (r/a))
    

def main():
    decrypt_keys = [modular_multi_inverse(CHAR_SET, key) for key in get_coprimes_less_than(CHAR_SET)]
    ciphertext = clean_input(input("Enter cipher text:"))
    plaintext_and_key = dict([(multiplicative_cipher(ciphertext, key), key) for key in decrypt_keys])
    plaintexts = list(plaintext_and_key.keys())
    plaintexts.sort(reverse=True,key=get_english)


    print("Guesses in decending order of likelihood:")
    for plaintext in plaintexts:
        print(f"Encryption key, decryption key: {modular_multi_inverse(CHAR_SET, plaintext_and_key[plaintext])}, {plaintext_and_key[plaintext]} || Plaintext: {plaintext} || English words: {get_english(plaintext)}")

if __name__ == "__main__":
    main()
