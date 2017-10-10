# Create a length 624 list to store the state of the generator

MT = [0 for i in xrange(624)]
index = 0

# To get last 32 bits
BITMASK_1 = (2 ** 32) - 1

# To get 32. bit
BITMASK_2 = 2 ** 31

# To get last 31 bits
BITMASK_3 = (2 ** 31) - 1

def initialize_generator(seed):
    "Initialize the generator from a seed"
    global MT
    global BITMASK_1
    MT[0] = seed
    for i in xrange(1,624):
        MT[i] = ((1812433253 * MT[i-1]) ^ ((MT[i-1] >> 30) + i)) & BITMASK_1

'''
Generates random integers between 0 and 2^32 
'''
def custom_random_integer():
    global index
    global MT
    if index == 0:
        generate_numbers()
    y = MT[index]
    y ^= y >> 11
    y ^= (y << 7) & 2636928640
    y ^= (y << 15) & 4022730752
    y ^= y >> 18

    index = (index + 1) % 624
    return y

def generate_numbers():
    "Generate an array of 624 untempered numbers"
    global MT
    for i in xrange(624):
        y = (MT[i] & BITMASK_2) + (MT[(i + 1 ) % 624] & BITMASK_3)
        MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
        if y % 2 != 0:
            MT[i] ^= 2567483615

def rand_int(start, end):
    return int(start + (1 + end - start) * custom_random_integer() / 2**32)
