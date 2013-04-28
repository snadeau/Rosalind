def string_slicer(string, a, b, c, d):
    """
    Inputs a string of length <=200 and four integers a, b, c, and d
    Returns a string from indices (a through b) and (c through d) with space
    in between, inclusively
    """

    if (len(string) <= 200):

        newString = string[a:b+1] + ' ' + string[c:d+1]
        return newString

    else:

        print "String is not less than or equal to 200 characters"


input_string = "ziq1IvJ1zG4BIidpyjmNoHI0m8hgvB4ADxcg8FIoFbSIVSkzO3c6QSorex6teLE04aijFbsOJstARtC9ncS7y4aIXk3WA6Aq21cvoMeXvlGjvSH1YBOVUx9ZfJyVhzKY7iRfHkc5NCnach0SXVPIHCj7YhyemalisUGUUNAJFHHxCB9J9u41YHl8Rb3VBmgy5rn."
print string_slicer(input_string, 53, 57, 153, 160)
