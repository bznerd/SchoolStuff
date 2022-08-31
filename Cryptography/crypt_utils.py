import math

def rail(index, rails):
   pos =  index % ((rails-1) * 2)
   if pos > rails-1:
       return (rails - 1) - (pos-(rails-1)) 
   else: return pos

def railfence_encipher(plaintext, num_rows):
    if num_rows not in [2,3]: raise ValueError("num_rows parameter to railfence_encipher must be 2 or 3")
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
    matrix = [['' for x in range(len(ciphertext))] for y in range(num_rows)]

    for x in range(len(ciphertext)):
        matrix[rail(x, num_rows)][x] = '*'


def caesar(message, key, encipher=True):
    pass

def text_block(message, size=5):
    for block in range(0, int(len(message)/5)+1):
        message = message[:block*6]+ ' ' + message[block*6:]
    return message[1:]

print(text_block(railfence_encipher("abcdefghijklmno" , 3)))
