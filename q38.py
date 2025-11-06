#  WAJP to print nth term of Fibonacci series by memoization technique.
class Solution:
    def nth_term_fibonacci(self,n):
        if n==1:
            return 0
        if n==2:
            return 1
        i=3

    
        n1=0
        n2=1
        while i<=n:
            n3=n1+n2
            n1=n2
            n2=n3
        
            i+=1
        return n3
    
ob1=Solution()
n=2
print(ob1.nth_term_fibonacci(n))