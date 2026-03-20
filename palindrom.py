# from audioop import reverse
#
# from pandas.conftest import string_dtype

string1=str(input("entr the sequence to check palindrom"))
# if(string1.casefold()==string1.casefold(reverse(string1))):
#     print(("yes ...it is a plaindrom sequence"))
# else:
#     a=''.join(string1+reverse(string1))
#     print(a)
rev=string1[::-1]
if(string1==rev):
    print("yes..it is palindrom")
else:
    print("no its not palindrom ...it might be done as ")
    a=''.join(string1+rev)
    print(a)
