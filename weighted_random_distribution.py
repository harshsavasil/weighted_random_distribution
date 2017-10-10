#!/usr/bin/env python2
from random_generation import rand_int, initialize_generator
from datetime import datetime
import argparse

if __name__ == "__main__":
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
    ap.add_argument("-t", "--total", type=int, default=100,
        help="Total number of samples")    
    args = vars(ap.parse_args())

    a = args.get('start')
    b = args.get('end')
    # import pdb; pdb.set_trace()
    if a > b:
        print "starting element cannot be greater than ending element."
    else:
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
            random_index = rand_int(0,total_weights-1)
            if random_index < weights['L']:
                random_lower_number.append(rand_int(a,(b+a)/2))
                random_number['L'] += 1 
            else:
                random_upper_number.append(rand_int((a+b+2)/2,b))
                random_number['H'] += 1
        print "low"
        print random_lower_number
        print "high"
        print random_upper_number
        print "count"
        print random_number