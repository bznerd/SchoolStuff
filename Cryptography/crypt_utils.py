"""
Found on github at https://github.com/bznerd/SchoolStuff/blob/master/Cryptography/crypt_utils.py
Written by Ben Campbell
"""
import math

GLOBAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rail(index, rails):
   pos =  index % ((rails-1) * 2)
   if pos > rails-1:
       return (rails - 1) - (pos-(rails-1)) 
   else: return pos


def strip(text, LETTERS=GLOBAL_LETTERS):
    return ''.join([char for char in text if char in LETTERS])


def gcd(a, b):
    if b > a:
        a += b
        b = a-b
        a -=b
    if a % b == 0: return b
    return gcd(b,a%b)


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


def railfence_encipher(plaintext, num_rows):
    if num_rows not in [2,3]: raise ValueError("num_rows parameter to railfence_encipher must be 2 or 3")
    plaintext = strip(plaintext.upper())
    cipher_grid = [[],[]]
    if num_rows == 3: cipher_grid.append([])
    for x, char in enumerate(plaintext):
        cipher_grid[rail(x, num_rows)].append(char)
    ciphertext = ''
    for row in cipher_grid:
        ciphertext += ''.join(row)
    return ciphertext


def railfence_decipher(ciphertext, num_rows):
    if num_rows not in [2,3]: raise ValueError("num_rows parameter to railfence_encipher must be 2 or 3")
    ciphertext = strip(ciphertext.upper())
    matrix = [['' for x in range(len(ciphertext))] for y in range(num_rows)]
    filled_matrix = matrix

    for x in range(len(ciphertext)):
        matrix[rail(x, num_rows)][x] = '*'

    index = 0
    for row, line in enumerate(matrix):
        for column, char in enumerate(line):
            if char == '*':
                filled_matrix[row][column] = ciphertext[index]
                index += 1

    return ''.join([filled_matrix[rail(x, num_rows)][x].lower() for x in range(len(ciphertext))]).lower()


def multiplicative_cipher(text, key, LETTERS=GLOBAL_LETTERS):
    return ''.join([LETTERS[int((LETTERS.find(char)*key)%len(LETTERS))] for char in text])


def caesar(message, key, encipher=True, LETTERS=GLOBAL_LETTERS):
    if not encipher:
        key = len(LETTERS)-key % len(LETTERS)
    
    if encipher: return ''.join([LETTERS[(LETTERS.find(char) + key) % len(LETTERS)] for char in message])
    return ''.join([LETTERS[(LETTERS.find(char) + key) % len(LETTERS)] for char in message])


def text_block(message, size=5):
    for block in range(0, int(len(message)/size)+1):
        message = message[:block*(size+1)]+ ' ' + message[block*(size+1):]
    return message[1:].upper()


def encipher_tabula_recta(plaintext, key, LETTERS=GLOBAL_LETTERS):
    ciphertext = ''
    for x, char in enumerate(plaintext):
        char_index = LETTERS.find(char.upper())
        ciphertext += LETTERS[(char_index + LETTERS.find(key[x])) % len(LETTERS)]

    return ciphertext


def decipher_tabula_recta(ciphertext, key, LETTERS=GLOBAL_LETTERS):
    plaintext = ''
    for x, char in enumerate(ciphertext):
        char_index = LETTERS.find(char.upper())
        plaintext += LETTERS[(char_index - LETTERS.find(key[x])) % len(LETTERS)]

    return plaintext


def encipher_vigenere(plaintext, key, LETTERS=GLOBAL_LETTERS):
    full_key =  key * (len(plaintext)//len(key)) + key[:len(plaintext)%len(key)]
    return encipher_tabula_recta(plaintext, full_key, LETTERS)


def decipher_vigenere(ciphertext, key, LETTERS=GLOBAL_LETTERS):
    full_key =  key * (len(ciphertext)//len(key)) + key[:len(ciphertext)%len(key)]
    return decipher_tabula_recta(ciphertext, full_key, LETTERS)


def vigenere(key, message, encipher=True, LETTERS=GLOBAL_LETTERS, autokey=False):
    if not autokey: full_key =  key * (len(message)//len(key)) + key[:len(message)%len(key)]
    
    if encipher:
        message = strip(message, LETTERS)
        if autokey: full_key = key + message[:len(message)-len(key)]
        return encipher_tabula_recta(message, full_key, LETTERS).upper()

    else:
        if autokey:
            full_key = key
            plaintext = ''
            for x, char in enumerate(message):
                char_index = LETTERS.find(char.upper())
                plaintext += LETTERS[(char_index - LETTERS.find(full_key[x])) % len(LETTERS)]
                if len(full_key) < len(message):
                    full_key += plaintext[-1]

            return plaintext.lower()

        else:
            return decipher_tabula_recta(message, full_key, LETTERS)


def gen_letter_combos(length, combos=[''], LETTERS=GLOBAL_LETTERS):
    if length == 1: return [string + char for string in combos for char in LETTERS]
    return gen_letter_combos(length-1, [string + char for string in combos for char in LETTERS], LETTERS)


def find_repeats(message, size=5, LETTERS=GLOBAL_LETTERS):
    repeats = []
    for string in gen_letter_combos(3, LETTERS=LETTERS):
        if message.count(string) > 1:
            for full_string in [string + two_len_string for two_len_string in gen_letter_combos(2, LETTERS=LETTERS)]:
                    if message.count(full_string) > 1: repeats.append(full_string)

    return repeats

def egcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = egcd(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    
    return gcd, x, y

def rsa(p, q, e):
    n = p*q
    phi = (p-1)*(q-1)
    gcd, d, y = egcd(e, phi)

    return n, phi, d%phi

def rsa_crypt(message, e, n):
    return (message**e)%n
