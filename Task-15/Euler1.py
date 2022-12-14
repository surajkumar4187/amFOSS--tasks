n = int (input ())
for i in range(n):
    a = int (input ())
    myList = []
    for i in range (2,a):
        if i%5 == 0 or i%3 == 0:
            myList.append(i)
    print (sum(myList))
