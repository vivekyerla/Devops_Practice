'''
Different implementations of python
- cpython = C implementation of python ... need to compile first
- jython = Java implementation of python ... need to compile first
- ironpython = .NET implementation of python ... no need to compile
- PyPy = fast, compliant alternative implementation of the Python language ... no need to compile
    
In Python, .py gets converted to .pyc and then is executed on python environment 
'''

# function definition
def print_multiplication_table(table, start, end):

    print("Hello World ... This is my first program")  # normal print

    for i in range(start,end):      # equivalent C syntax - for (i = 1; i<11; i++)

        print(f"{table} * {i} = {table * i}")       # will work on python 3 .. not on python 2
        #  Curly braces are used to evaluate any expression
        # f is for formatted syntax available in python 3 not on python 2

        print ("{0} * {1} = {2}".format(table, i, table * i))   # will work on python 2 and python 3
        # Same operation in different technique

print_multiplication_table(5,1,11)      # function call









