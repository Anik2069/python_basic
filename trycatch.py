
try:
    num=int(input ("Enter a number: "))
    print(num)
except ValueError as err:
    print(err)
