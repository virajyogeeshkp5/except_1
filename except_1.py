try:
    str = 'rahul'         # This is store the name form variable
    n=len(str)            # Length of the string
    while n>0:            # While condition  n is greater than 0
        print(str[n])     # str with nth value
        n=n-1
except Exception as err:
    print("This is some error iterating:",err)
finally:
    print("Hello")