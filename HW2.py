def intersection_of_complements(A, B, U):
    # inputs: A, B and U are of type 'set'
    # output: a tuple of the form (set, set)

    #
    # YOUR CODE HERE
    #
    A_complements = U - A
    B_complements = U - B
    return(A_complements, A_complements & B_complements)

A = set([-6, 3, 4, 5])
B = set([-6, 5, 13])
U = A|B|set([12,-2,-4])

intersection_of_complements(A,B,U)
