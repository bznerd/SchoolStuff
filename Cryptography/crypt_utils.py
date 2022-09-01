"""
Found on github at https://github.com/bznerd/SchoolStuff/blob/master/Cryptography/crypt_utils.py
Written by Ben Campbell
"""
import math

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHAR_SET = 26

def rail(index, rails):
   pos =  index % ((rails-1) * 2)
   if pos > rails-1:
       return (rails - 1) - (pos-(rails-1)) 
   else: return pos


def strip(text):
    return ''.join([char for char in text if char.upper() in LETTERS])


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


def multiplicative_cipher(text, key):
    return ''.join([LETTERS[int((LETTERS.find(char.upper())*key)%CHAR_SET)] for char in text]).lower()


def caesar(message, key, encipher=True):
    if not encipher:
        key = CHAR_SET-key % CHAR_SET
    
    message = strip(message)
    if encipher: return ''.join([LETTERS[(LETTERS.find(char.upper()) + key) % CHAR_SET] for char in message])
    return ''.join([LETTERS[(LETTERS.find(char.upper()) + key) % CHAR_SET] for char in message]).lower()


def text_block(message, size=5):
    for block in range(0, int(len(message)/size)+1):
        message = message[:block*(size+1)]+ ' ' + message[block*(size+1):]
    return message[1:]
