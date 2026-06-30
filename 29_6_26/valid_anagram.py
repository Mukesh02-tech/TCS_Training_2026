def isAnagram(s,t):
    s=sorted(s)
    t=sorted(t)
    if len(s)==len(t) and s==t:
        return True
    else:
        return False

s=input()
t=input()
if isAnagram(s,t):
    print("These 2 inputs are Valid Anagram")
else:
    print("These 2 inputs are not Valid Anagram")