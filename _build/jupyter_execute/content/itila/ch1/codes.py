import numpy as np
import itertools
from tqdm import tqdm

num_source_bits = 2

source_bits = np.random.choice([0, 1], num_source_bits, replace=True)

print(source_bits)

G_T = np.array([[1, 0],
                [0, 1],
                [1, 0],
                [1, 0],
                [1, 1],
                [1, 1],
                [0, 1],
                [0, 1]])

H = np.array([[1, 0, 1, 0, 0, 0, 0, 0],
              [1, 0, 0, 1, 0, 0, 0, 0],
              [1, 1, 0, 0, 1, 0, 0, 0],
              [1, 1, 0, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 1]])

def encode(source):
    return np.dot(G_T, source) % 2

transmitted = encode(source_bits)

def parities(received):
    return np.dot(H, received) % 2

parities(transmitted)

syndromes = [(0, 1)] * 6
syndromes = list(itertools.product(*syndromes))

codes = [(0, 1)] * 8
codes = list(itertools.product(*codes))

decode_dict = {}


for syndrome in syndromes:
    
    for code in codes:
        
        code_syndrome = np.dot(H, code) % 2
        num_bits = np.sum(code)
            
        syndrome_tup = tuple(syndrome)
        code_syndrome_tup = tuple(code_syndrome)
        
        if syndrome_tup == code_syndrome_tup:
            
            if syndrome_tup in decode_dict:
                
                if (num_bits < decode_dict[syndrome_tup][1]):
                    decode_dict[syndrome_tup] = (code, num_bits)
                
            else:
                decode_dict[syndrome_tup] = (code, num_bits)
                
# for k, v in decode_dict.items():
#     print(k, v)
                
decode_dict = {k : v[0] for k, v in decode_dict.items()}

def decode(received):
    
    syndrome = np.dot(H, received) % 2
    
    noise = decode_dict[tuple(syndrome)]
    
    decoded = (received + noise) % 2
    
    return decoded, syndrome, noise

num_trans = int(1e5)
flip_prob = 1e-1

total_errors = 0
total_bits = 2 * num_trans

for n in range(num_trans):
    
    source_bits = np.random.choice([0, 1], num_source_bits, replace=True)
    
    encoded = encode(source_bits)
    
    noise = np.random.choice([0, 1], len(encoded), p=[1 - flip_prob, flip_prob], replace=True)
    num_noisy = np.sum(noise)
    
    transmitted = (encoded + noise) % 2
    
    decoded, syndrome, decoded_noise = decode(transmitted)
    
    num_errors = np.sum(encoded[:2] != decoded[:2])
    
    if num_noisy <= 2 and num_errors != 0:
        print(num_noisy, num_errors)
    
    total_errors = total_errors + num_errors
    
print(total_errors / total_bits)

n = 1000

n / (n + 2 + 2 * n)

G_T = np.array([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 1]])

H = np.array([[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

def encode(source):
    return np.dot(G_T, source) % 2


def decode(received):
    
    syndrome = np.dot(H, received) % 2
    
    noise = decode_dict[tuple(syndrome)]
    
    decoded = (received + noise) % 2
    
    return decoded, syndrome, noise

syndromes = [(0, 1)] * 10
syndromes = list(itertools.product(*syndromes))

codes = [(0, 1)] * 14
codes = list(itertools.product(*codes))

decode_dict = {}

for syndrome in tqdm(syndromes):
    
    for code in codes:
        
        code_syndrome = np.dot(H, code) % 2
        num_bits = np.sum(code)
            
        syndrome_tup = tuple(syndrome)
        code_syndrome_tup = tuple(code_syndrome)
        
        if syndrome_tup == code_syndrome_tup:
            
            if syndrome_tup in decode_dict:
                
                if (num_bits < decode_dict[syndrome_tup][1]):
                    decode_dict[syndrome_tup] = (code, num_bits)
                
            else:
                decode_dict[syndrome_tup] = (code, num_bits)
                
# for k, v in decode_dict.items():
#     print(k, v)
                
decode_dict = {k : v[0] for k, v in decode_dict.items()}

num_source_bits = 4
flip_prob = 1e-1

num_trans = int(1e4)
total_errors = 0
total_bits = num_source_bits * num_trans

for n in range(num_trans):
    
    source_bits = np.random.choice([0, 1], num_source_bits, replace=True)
    
    encoded = encode(source_bits)
    
    noise = np.random.choice([0, 1], len(encoded), p=[1 - flip_prob, flip_prob], replace=True)
    num_noisy = np.sum(noise)
    
    transmitted = (encoded + noise) % 2
    
    decoded, syndrome, decoded_noise = decode(transmitted)
    
    num_errors = np.sum(encoded[:num_source_bits] != decoded[:num_source_bits])
    
    if num_noisy <= 2 and num_errors != 0:
        print(num_noisy, num_errors)
        
    if num_noisy == 3 and num_errors > 0:
        print(noise)
    
    total_errors = total_errors + num_errors
    
print(total_errors / total_bits)

# General encoder-decoder

def build_decode_dict(H, syndrome_size, code_size):
    
    # All possible syndromes
    syndromes = [(0, 1)] * syndrome_size
    syndromes = list(itertools.product(*syndromes))

    # All possible codes
    codes = [(0, 1)] * code_size
    codes = list(itertools.product(*codes))

    # Decode dictionary to store {syndrome : code} pairs
    decode_dict = {}

    # For each syndrome, code with least 1s which produces the syndrome
    for syndrome in tqdm(syndromes):
        
        syndrome_tup = tuple(syndrome)

        # Loop over all codes, to find the code with least 1s
        for code in codes:
            
            # Num bits in code
            num_bits = np.sum(code)
            
            # Syndrome produced by the code
            code_syndrome = np.dot(H, code) % 2
            code_syndrome_tup = tuple(code_syndrome)

            # If syndrome patterns match, replace code if better than previous
            if syndrome_tup == code_syndrome_tup:

                if syndrome_tup in decode_dict:

                    if (num_bits < decode_dict[syndrome_tup][1]):
                        decode_dict[syndrome_tup] = (code, num_bits)

                else:
                    decode_dict[syndrome_tup] = (code, num_bits)

    # Take out the bit-numbers
    decode_dict = {k : v[0] for k, v in decode_dict.items()}
    
    return decode_dict


def encode(source, G_T):
    return np.dot(G_T, source) % 2


def decode(received, H, decode_dict):
    
    syndrome = np.dot(H, received) % 2
    
    noise = decode_dict[tuple(syndrome)]
    
    decoded = (received + noise) % 2
    
    return decoded, syndrome, noise

# The (8, 2) code

syndrome_size = 6
code_size = 8

G_T = np.array([[1, 0],
                [0, 1],
                [1, 0],
                [1, 0],
                [1, 1],
                [1, 1],
                [0, 1],
                [0, 1]])

H = np.array([[1, 0, 1, 0, 0, 0, 0, 0],
              [1, 0, 0, 1, 0, 0, 0, 0],
              [1, 1, 0, 0, 1, 0, 0, 0],
              [1, 1, 0, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 1]])

decode_dict = build_decode_dict(H, syndrome_size=syndrome_size, code_size=code_size)

num_trans = int(1e5)
flip_prob = 1e-1

total_errors = 0
total_bits = 2 * num_trans

for n in range(num_trans):
    
    source_bits = np.random.choice([0, 1], num_source_bits, replace=True)
    
    encoded = encode(source_bits, G_T)
    
    noise = np.random.choice([0, 1], len(encoded), p=[1 - flip_prob, flip_prob], replace=True)
    num_noisy = np.sum(noise)
    
    transmitted = (encoded + noise) % 2
    
    decoded, syndrome, decoded_noise = decode(transmitted, H, decode_dict)
    
    num_errors = np.sum(encoded[:2] != decoded[:2])
    
    if num_noisy <= 2 and num_errors != 0:
        print(num_noisy, num_errors)
    
    total_errors = total_errors + num_errors
    
print(f'p(bit error) {total_errors / total_bits} rate {(code_size - syndrome_size)/code_size}')

# The (14, 4) code

syndrome_size = 10
code_size = 14

G_T = np.array([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 1]])

H = np.array([[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

decode_dict = build_decode_dict(H, syndrome_size=syndrome_size, code_size=code_size)

num_source_bits = 4
num_trans = int(1e5)
flip_prob = 1e-1

total_errors = 0
total_bits = num_source_bits * num_trans

for n in range(num_trans):
    
    source_bits = np.random.choice([0, 1], num_source_bits, replace=True)
    
    encoded = encode(source_bits, G_T)
    
    noise = np.random.choice([0, 1], len(encoded), p=[1 - flip_prob, flip_prob], replace=True)
    num_noisy = np.sum(noise)
    
    transmitted = (encoded + noise) % 2
    
    decoded, syndrome, decoded_noise = decode(transmitted, H, decode_dict)
    
    num_errors = np.sum(encoded[:num_source_bits] != decoded[:num_source_bits])
    
    if num_noisy <= 2 and num_errors != 0:
        print(num_noisy, num_errors)
    
    total_errors = total_errors + num_errors
    
print(f'p(bit error) {total_errors / total_bits} rate {(code_size - syndrome_size)/code_size}')

# The (14, 6) code

syndrome_size = 8
code_size = 14

G_T = np.array([[1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 1]])

H = np.array([[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]])

decode_dict = build_decode_dict(H, syndrome_size=syndrome_size, code_size=code_size)

num_source_bits = 6
num_trans = int(1e5)
flip_prob = 1e-1

total_errors = 0
total_bits = num_source_bits * num_trans

for n in range(num_trans):
    
    source_bits = np.random.choice([0, 1], num_source_bits, replace=True)
    
    encoded = encode(source_bits, G_T)
    
    noise = np.random.choice([0, 1], len(encoded), p=[1 - flip_prob, flip_prob], replace=True)
    num_noisy = np.sum(noise)
    
    transmitted = (encoded + noise) % 2
    
    decoded, syndrome, decoded_noise = decode(transmitted, H, decode_dict)
    
    num_errors = np.sum(encoded[:num_source_bits] != decoded[:num_source_bits])
    
    total_errors = total_errors + num_errors
    
print(f'p(bit error) {total_errors / total_bits} rate {(code_size - syndrome_size)/code_size}')

# The (12, 6) code

syndrome_size = 6
code_size = 12

G_T = np.array([[1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 1],
                [1, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 0, 0],
                [1, 0, 1, 1, 1, 0],
                [0, 0, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 1]])

H = np.array([[1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
              [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
              [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1]])

decode_dict = build_decode_dict(H, syndrome_size=syndrome_size, code_size=code_size)

num_source_bits = 6
num_trans = int(1e5)
flip_prob = 1e-1

total_errors = 0
total_bits = num_source_bits * num_trans

for n in range(num_trans):
    
    source_bits = np.random.choice([0, 1], num_source_bits, replace=True)
    
    encoded = encode(source_bits, G_T)
    
    noise = np.random.choice([0, 1], len(encoded), p=[1 - flip_prob, flip_prob], replace=True)
    num_noisy = np.sum(noise)
    
    transmitted = (encoded + noise) % 2
    
    decoded, syndrome, decoded_noise = decode(transmitted, H, decode_dict)
    
    num_errors = np.sum(encoded[:num_source_bits] != decoded[:num_source_bits])
    
    total_errors = total_errors + num_errors
    
    if num_noisy <= 2 and num_errors != 0:
        input(f'{noise} {syndrome} {np.dot(H, noise) % 2} {np.dot(H, decoded_noise) % 2} {num_errors} {num_noisy}')
    
print(f'p(bit error) {total_errors / total_bits} rate {(code_size - syndrome_size)/code_size}')

np.dot(H, np.dot(G_T, source_bits))

