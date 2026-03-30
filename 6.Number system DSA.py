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
        b=x
        if x<0:
            x=-x
        a=str(x)
        s=a[::-1]
        s=int(s)
        if b<0:
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
#50. Pow(x, n)
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
        import math
        a=int(math.sqrt(x))
        if x<0 or x>2**31 - 1:
            return 0
        return a
#136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int: # type: ignore
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
#504. Base 7
class Solution:
    def convertToBase7(self, num: int) -> str:
        s=""
        a=num
        if num==0:
            return "0"
        if num<0:
            num=-num
        while num>0:
            n=num%7
            num=num//7
            s=str(n)+s
        if a<0:
            s="-"+s
        return s
#593. Valid Square
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool: # type: ignore
        def dist(a,b):
            return (a[0]-b[0])**2+(a[1]-b[1])**2
        points=[p1,p2,p3,p4]
        s=set()
        for i in range(4):
            for j in range (i+1,4):
                d=dist(points[j],points[i])
                if d==0:
                    return False
                s.add(d)
        return len(s)==2
#633. Sum of Square Numbers
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        a=0
        b=int(math.sqrt(c))
        while a<=b:
            s=a*a+b*b
            if s==c:
                return True
            elif s<c:
                a+=1
            else:
                b-=1
        return False
#202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        p=set()
        while n!=1 and n not in p:
            p.add(n)
            a=str(n)
            s=0
            for i in range(len(a)):
                b=int(a[i])**2
                s+=b
            n=s
        return n==1
#306: Additive Number
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1,len(num)):
            for j in range(i+1,len(num)):
                a=num[:i]
                b=num[i:j]
                if (a.startswith('0') and len(a)>1 or b.startswith('0') and len(b)>1):
                    continue
                x,y=int(a),int(b)
                k=j
                while k<len(num):
                    s=x+y
                    s_str=str(s)
                    if not num.startswith(s_str,k):
                        break
                    k+=len(s_str)
                    x,y=y,s
                if k==len(num):
                    return True
        return False
#400: Nth digit 
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9
        start = 1
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        number = start + (n - 1)//digit_length
        digit_index = (n - 1) % digit_length

        return int(str(number)[digit_index])
