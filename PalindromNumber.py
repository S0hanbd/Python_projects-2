class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = []
        x = str(x)
        for i in range(len(x)//2):
            print(x[i], x[-i])
            if x[i] != x[-i]:
                print("this",x[i],x[len(x)-i], len(x), i)
                return False
        return True

s = Solution()
print(s.isPalindrome(81218))