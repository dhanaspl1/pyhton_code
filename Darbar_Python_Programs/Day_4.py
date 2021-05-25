'''
Given an array A of size N, print the reverse of it.

Input:
First line contains an integer denoting the test cases 'T'. T testcases follow. Each testcase contains two lines of input. First line contains N the size of the array A. The second line contains the elements of the array.

Output:
For each testcase, in a new line, print the array in reverse order.

Constraints:
1 <= T <= 100
1 <= N <=100
0 <= Ai <= 100

Example:
Input:
1
4
1 2 3 4
Output:
4 3 2 1

'''
# Solution : 1

a = int(input())

for i in range(a) :
    b = int(input())
    c=[]
    for j in range(b):
        c.insert(j,input())
    d = c[::-1]
    print(*d)
    if a == 1:
        break

# Solution : 2

a = int(input())

for i in range(a) :
    b = int(input())
    c = str(input()).split(' ')
    d = c[::-1]
    d = ' '.join(d)
    print(d.strip())
    if a == 1:
        break