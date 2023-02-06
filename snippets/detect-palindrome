# Wrote isPalindrome on my own,
# and removePunct from memory after 
# seeing example in Lecture 6


def isPal(s):
    def isPalindrome(s):
            if len(s) <= 0: 
                return True
            else:
                return s[0] == s[-1] and isPalindrome(s[1:-1])
            
    def removePunct(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans
    
    return isPalindrome(removePunct(s))
