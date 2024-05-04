class Solution(object):
    def isPalindrome(self, s):
        s= re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        rev_s=s[::-1]
        
        if s==rev_s:
            return True
        else:
            return False
        