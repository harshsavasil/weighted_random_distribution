# weighted_random_distribution
Weighted Random number generation.
The script can be used to generate random numbers between a given range a and b. 
BY Default elemnets in lower half of range have lower probability, by default it is 27%, for equal distribution just set probability of both upper and lower half equal to 50. 
## Run python weighted_random_distribution.py --help to seek help about the parameters.
List of Parameters - <br/>
--start - start of range. Default value is 1 and type is integer. <br/>
--end - end of range. Default values is 10 and type is integer. <br/>
--total - total number of random numbers you want to generate. <br/>
--lower - probability of elements of lower half. <br/>
--upper - probability of elements of upper half. <br/>

There is no third party function used for generating random numbers , I have used 'Mersenne Twister' algorithm for generating pseudo random numbers. The Mersenne Twister is one of the most extensively tested random number generators in existence.
Based on the pseudocode in https://en.wikipedia.org/wiki/Mersenne_Twister. Generates uniformly distributed 32-bit integers in the range [0, 232 − 1] with the MT19937 algorithm.
