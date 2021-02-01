n = int(input("Enter a number"))
n1 = 1  # For true case
val = input("Enter 0 for false and 1 for true")

# boolval = True
if val == "0":
    boolval: bool = False
elif val == "1":
    boolval: bool = True

while n > 0 and n1 <= n:
    if boolval == False:
        print(n * "*")
        n -= 1
    else:
        print(n1 * "*")
        n1 += 1
    # print()


