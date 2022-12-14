import math

n = int (input ())

for k in range(n):
    a = int(input())

    answer= 0
    while a % 2 == 0:
        answer = 2
        a = a/2    

    for i in range(3, int(math.sqrt(a)) + 1, 2):
        while a % i == 0:
            answer = i
            a = a / i
    if a > 2:
        answer = a

    print(int(answer))
  
