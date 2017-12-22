def reverse(x):#x is an integer
#when x not in range(-2,147,483,648 , 2,147,483,647) return 0
    string = str(x)
    if x not in range(-2147483648, 2147483647):
        num =  0
    elif x < 0:
        ls = []
        i = 0
        string = string[1:]
        while i < len(string):
            ls.append(string[len(string) - (i + 1)])
            i = i + 1
            num = -int( "".join(ls))
    elif x >= 0:
        ls = []
        i = 0
        while i < len(string):
            ls.append(string[len(string) - (i + 1)])
            i = i + 1
        num =int( "".join(ls))
    return num


print(reverse(4830))
print(reverse(-38349))
print(reverse(123))
print(reverse(0))
# string = str(45342)
# print(string)
# #print(len(string))
# i = 0
# ls = []
# #print(string[0])
# while i<len(string):
#     print( string[len(string)-(i+1)])
#     ls.append(string[len(string)-(i+1)])
#     i = i+1
# print(ls)
# num_str = "".join(ls)
# print(num_str)
# out = int(num_str)
# print(out)