n = int(input("Enter a number"))
n1 = 1  # For true case
boolval = bool(int(input("Enter 0 for false and 1 for true")))  # take a input then (typecast) change into integer and lastly (typecast) change into boolean 

while n > 0 and n1 <= n:
    if boolval == False:
        print(n * "*")
        n -= 1
    else:
        print(n1 * "*")
        n1 += 1
    # print()


