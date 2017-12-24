def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    list_s = list(map(str, s))
    list_s1 = list(map(str, s))#way to split string without spaces into list
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
    'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    num = 0
    while True:
        try:
            if list_s[0]+list_s[1] in d.keys():
                print(list_s)
                num = num + d["".join(list_s[0]+list_s[1])]
                print("".join(list_s[0]+list_s[1]))
                list_s.pop(0)
                list_s.pop(0)
            else:
                print(list_s)
                num = num + d[list_s[0]]
                list_s.pop(0)
        except:
            if len(list_s)==1:
                num = num + d[list_s[0]]
            break
    return num
