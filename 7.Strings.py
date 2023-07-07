#isomorphic strings
def isIsomorphic(self, s: str, t: str) -> bool:
        s,t = list(s),list(t)
        DicS,DicT ={},{}
        for c1,c2 in zip(s,t):
            if ((c1 in DicS and DicS[c1]!=c2) or (c2 in DicT and DicT[c2]!=c1)):
                return False
            DicS[c1] = c2
            DicT[c2]= c1
        return True
#strbomatic number
def isStrobogrammatic(nums):
    l = 0
    r = len(nums)-1

    while (l<=r):
        nums1 = int(nums[l])
        nums2 = int(nums[r])
        if ((nums1 not in [0,1,6,8,9]) or (nums1 ==nums2 and nums1 not in [0,1,8]) or 
            (nums1==6 and nums2!=9) or (nums2==9 and nums1!=6)):
            return False
        l+=1
        r-=1
    return True
nums=[9,8,6]
print(isStrobogrammatic(nums))
# Add strings
def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ''
        carry= 0
        if len(num1)>len(num2):
            num2 += '0'*(len(num1)-len(num2))
        else:
            num1 += '0'*(len(num2)-len(num1))
        for i in range(len(num1)):
            digit_sum = int(num1[i])+int(num2[i])+carry
            carry = digit_sum//10
            res += str(digit_sum%10)
        if carry>0:
            res += str(carry)
        return res[::-1]
#reverse only words
def reverseWords(self, s: str) -> str:
        words =s.split()
        ans = ''
        for i in range(len(words)):
            ans+=words[i][::-1]
            if i!=len(words)-1:
                ans+=' '
        return ans
#5. REVERSE K NUMBER STRINGS
def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
#6.Rotate array
def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!= len(goal):
            return False
        s , goal = [*s],[*goal]
        for i in range(len(s)):
            a = s[0]
            s.pop(0)
            s.append(a)
            if s == goal:
                return True 
        return False
#7.check strings
def backspaceCompare(self, s: str, t: str) -> bool:
        def built(s):
            ans = []
            for n in s:
                if n!='#':
                    ans.append(n)
                elif ans:
                    ans.pop()
            return ''.join(ans)
        return built(s)==built(t)
