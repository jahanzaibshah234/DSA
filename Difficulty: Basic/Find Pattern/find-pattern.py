def findPattern(s,p):
    #code here
    if p in s:
        return s.index(p)
    else:
        return -1