# from curses.ascii import isdigit
from curses.ascii import isdigit

num=str(input("enter the the number of credit chard"))
if(len(num)==19):
    # for c in num:
    # if all(c.isdigit() or c == '-' for c in num):
        mask=''.join("*"if c.isdigit() else c for c in num[:-4])+num[-4:]
        print(mask)
#     for i in range(-19,-4):
#         if(isdigit(num[i])):
#             print("*")
#         else:
#             print(num[i])
#     for j in range(-4,0):
#         print(num[j])
# else:
#     print("the num is not valid")