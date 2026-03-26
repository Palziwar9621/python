#7. Reverse Integer
class Solution:
    def reverse(self, x: int):
        a=x
        if x<0:
            x=-x
        i=len(str(x))
        s=0
        for _ in range(i):
            y=x%10
            s=y+s*10
            x=x//10
        if a<0:
           s=-s
        if s<-2**31 or s>2**31-1:
            return 0
        return s
class Solution:
    def reverse(self, x: int):
        if x<0:
            x=-x
        a=str(x)
        s=a[::-1]
        s=int(s)
        if x<0:
            s=-s
        if s<-2**31 or s>2**31-1:
            return 0
        return s
#9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=x
        if x<0:
            x=-x
        b=str(x)
        s=int(b[::-1])
        return s==a
#29. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        a=x**n
        if x<-100.0 or x>100.0:
            return 0
        if n<-2**31 or n>2**31 - 1:
            return 0
        if a<-10**4 or a>10**4:
            return 0
        return a
#69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        import cmath
        a=int(sqrt(x))
        if x<0 or x>2**31 - 1:
            return 0
        return a
#136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in nums:
            if nums.count(x)!=2:
                return x
#231. Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n<=0:
            return False
        if n<-2**31 or n>2**31-1:
            return False
        x=math.log2(n)
        return x.is_integer()
#258. Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            a = len(str(num))
            for _ in range(a):
                b = num // 10**(a-1) 
                s += b
                num = num % 10**(a-1) 
                a -= 1
            num = s
        return num
#263. Ugly Number
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        while n%2==0:
            n=n//2
        while n%3==0:
            n=n//3
        while n%5==0:
            n=n//5
        if n==1:
            return True
        else:
            return False
#326. Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            while n%3==0:
                n=n//3
            if n==1:
                return True
            else:
                return False
#342. Power of Four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            while n%4==0:
                n=n//4
            if n==1:
                return True
            else:
                return False