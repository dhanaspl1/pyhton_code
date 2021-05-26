t = int(input());
for i in range(t):
    b = int(input())
	arr = str(input()).split(' ')
	sum = 0
	for n in range(b):
	    sum += (int(arr[n])*int(arr[n]) - int(arr[n+1])*int(arr[n+1]))
	    n=n+1
	    if n == (b-1):
	       break
	print(sum)
    if t == 1:
        break