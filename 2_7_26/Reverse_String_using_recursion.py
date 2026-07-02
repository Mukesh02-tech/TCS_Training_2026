def st(b,s):
    if s=="":
        return b
    b+=s[len(s)-1]
    s=s[:len(s)-1]
    return st(b,s)
s=input().strip()
print(st("",s))