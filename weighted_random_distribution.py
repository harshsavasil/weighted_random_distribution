#!/usr/bin/env python2

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


def custom_random_integer(start, end):
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
    return int(start + (1 + end - start) * y / 2**32)

def generate_numbers():
    "Generate an array of 624 untempered numbers"
    global MT
    for i in xrange(624):
        y = (MT[i] & BITMASK_2) + (MT[(i + 1 ) % 624] & BITMASK_3)
        MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
        if y % 2 != 0:
            MT[i] ^= 2567483615

if __name__ == "__main__":
    from datetime import datetime
    import argparse

    now = datetime.now()
    initialize_generator(now.microsecond)
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--start", type=int, default=1,
        help="starting element of range")
    ap.add_argument("-e", "--end", type=int, default=10,
        help="ending element of range")
    ap.add_argument("-l", "--lower", type=int, default=27,
        help="probability of lower half elements of given range")
    ap.add_argument("-u", "--upper", type=int, default=73,
        help="probability of upper half elements of given range")
    ap.add_argument("-t", "--total", type=int, default=100000,
        help="Total number of samples")    
    args = vars(ap.parse_args())

    a = args.get('start')
    b = args.get('end')
    weights = {
        "L": args.get('lower'), # assuming we have 100 samples , we want 27 out of them to be lower than half
        "H": args.get('upper')  # and 73 of them to be greater than half. These are hard-coded as per the question.  
    }
    total_weights = sum(weights.values())
    random_number = dict()   # for maintaining count of randomly selected lower or half elements of range. 
    random_lower_number = [] # for pushing randomly selected lower half elements
    random_upper_number = [] # for pushing randomly selected upper half elements
    random_number['L'] = 0   #initial count is set to zero.
    random_number['H'] = 0   # "L" is for lower half. "H" is for Upper half.

    for i in xrange(args.get('total')):
        random_index = custom_random_integer(0,total_weights-1)
        if random_index < weights['L']:
            random_lower_number.append(custom_random_integer(a,(b+a)/2))
            random_number['L'] += 1 
        else:
            random_upper_number.append(custom_random_integer((a+b+2)/2,b))
            random_number['H'] += 1
    print "low"
    print random_lower_number
    print "high"
    print random_upper_number
    print "count"
    print random_number