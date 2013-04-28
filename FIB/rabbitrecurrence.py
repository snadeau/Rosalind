#Scott Nadeau
#Rosalind
#Rabbits and Recurrence Relations


def rabbit_recurrence(num_months, litter_size):
    """
    Input number of months and litter size
    Return total number of rabbit pairs that will be present after number of
    months if each pair of reproduction-age rabbits produces given litter size
    in each generation. Similar to Fibonacci sequence but with varying litter
    size.
    """

    month = 0

    while month < num_months:
        if (month == 0):
            immature = 1
            mature = 0
        elif (month == 1):
            immature = 0
            mature = 1
        else:
            #calculate next gen offspring pairs based on current mature pair
            immature_temp = mature * litter_size
            #calculate and set next gen mature pairs based on current immature pairs
            mature = immature + mature
            #set number of next gen immature pairs
            immature = immature_temp

        month += 1

    return mature + immature

print rabbit_recurrence(32,3)
        
