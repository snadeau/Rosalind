#Scott Nadeau
#2013-04-26
#Rosalind
#Conditions and Loops

def sum_odd_integers(a, b):
    """
    Input two positive integers such that a < b < 10000
    Returns the sum of all odd integers from a through b inclusively
    """

    sum = 0
    
    while a <= b:
        if (a % 2 == 1):
            sum += a
        a += 1

    return sum

print sum_odd_integers(4939,9469)

        

