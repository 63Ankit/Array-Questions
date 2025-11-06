#  WAPP to store n terms of Fibonacci series into an array.
class Solution:
    def nth_term_fibonacci(self,n):
        if n==1:
            return [0]
        if n==2:
            return [0,1]
        i=3
        arr=[0]*(n)
        arr[1]=1
        j=2
        n1=0
        n2=1
        while i<=n:
            n3=n1+n2
            arr[j]=n3
            n1=n2
            n2=n3
            j+=1
            i+=1
        return arr
    
ob1=Solution()
n=10
print(ob1.nth_term_fibonacci(n))





