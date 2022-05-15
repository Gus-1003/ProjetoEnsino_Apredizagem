num = 7

if num > 0:
    for i in range(2, num):
        print(i)
        if (num % i) == 0:
            print ("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")