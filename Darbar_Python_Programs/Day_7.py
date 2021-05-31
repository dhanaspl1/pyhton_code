'''
Counting frequencies of array elements
Difficulty Level : Easy
Last Updated : 26 May, 2021
Given an array which may contain duplicates, print all elements and their frequencies.
Examples: 
 

Input :  arr[] = {10, 20, 20, 10, 10, 20, 5, 20}
Output : 10 3
         20 4
         5  1

Input : arr[] = {10, 20, 20}
Output : 10 1
         20 2
'''

arr = [10, 20, 20, 10, 10, 20, 5, 20, 5, 8, 3]
b = []
for i in arr:
    if(i not in b):
        b.append(i)
    print(b)
    print(arr)
for c in b:
    j = 0
    for a in arr:
        if c == a:
            j = j + 1
    print(c,j)


'''
Given an array A[] of N positive integers which can contain integers from 1 to P where elements can be repeated or can be absent from the array. Your task is to count the frequency of all elements from 1 to N.


Example 1:

Input:
N = 5
arr[] = {2, 3, 2, 3, 5}
P = 5
Output:
0 2 2 0 1
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.


class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        i = 1
        ar = arr
        b = []
        while i<=P:
            j = 0
            for a in ar:
                if i == a:
                    j = j + 1
            if i<=N:
                b.append(j)
            i = i + 1
        while P < N:
            b.append(0)
            P = P + 1
        print (*b)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends

'''