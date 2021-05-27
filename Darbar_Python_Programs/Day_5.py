t = int(input())
for i in range(t):
    b = int(input())
    arr = str(input()).split(' ')
    a = 0
    d = 0
    sum = 0
    if b == 2 :
        sum = (int(arr[0])*int(arr[0]))-(int(arr[1])*int(arr[1]))
        print(abs(sum))
    else :
        for n in range(b):
            if n%2 == 0 :
                a += int(arr[n])*int(arr[n]) 
            else :
                d += int(arr[n])*int((arr[n]))
            if n == (b-1):
                break
        sum = a - d
        print(sum)
    if t == 1:
        break