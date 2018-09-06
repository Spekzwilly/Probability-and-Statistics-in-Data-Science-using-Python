# modify this cell
from numpy import random
def seq_sum(n):
    """ input: n, generate a sequence of n random coin flips
        output: return the number of heads
        Hint: For simplicity, use 1,0 to represent head,tails
    """
    #
    # YOUR CODE HERE
    #
    heads = 0
    for num in range(n):
        if random.rand() <= 0.5:
            heads = heads
        else:
            heads += 1
    return heads

x = seq_sum(100)
print(x)
print([seq_sum(2) for x in range(20)])
#print(seq_sum(2))

# Modify this cell

def estimate_prob(n,k1,k2,m):
    """Estimate the probability that n flips of a fair coin result in k1 to k2 heads
         n: the number of coin flips (length of the sequence)
         k1,k2: the trial is successful if the number of heads is
                between k1 and k2-1
         m: the number of trials (number of sequences of length n)

         output: the estimated probability
         """
    #
    # YOUR CODE HERE
    #
    count = 0
    for rnd in range(m):
        if k1 <= seq_sum(n) < k2:
            count += 1
        else:
            count = count
    return float(count / m)

x = estimate_prob(100, 40, 60, 1000)
print(x)
assert 'float' in str(type(x))
