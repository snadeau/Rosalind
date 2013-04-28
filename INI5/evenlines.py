#Scott Nadeau
#2013-04-26
#Rosalind
#Working with Files

def even_num_lines_file(file):
    """
    Input a file and return a file named 'output.txt' containing the
    even-numbered lines from the input file
    """
    w = open('output.txt', 'w')

    line_num = 0

    list_of_lines = f.readlines()

    while (line_num < len(list_of_lines)):
        if (line_num % 2 == 1):
            w.write(list_of_lines[line_num])
        line_num += 1

    w.close()


f = open('input.txt', 'r')

even_num_lines_file(f)

f.close()

