###for countin the repetition
from itertools import count

l1=['10','20','30','40','50','10','20','40','50','60','90']
l2=[]
for i in l1:
    x=l1.count(i)
    l2.append(i)
    l2.append(x)
print(l2)
from operator import concat
###for the intersection operation
# l1=[10,20,30,40,50,10,20,40,50,60,90]
# l2=[10,50,60,90]
# l3=[]
# for i in l1:
#     if i in l2:
#         if i in l3:
#             continue
#         l3.append(i)
# print(l3)


###removing the same items in the list
# l1=[10,20,30,40,50,10,20,40,50,60,90]
# # for x in range(len(l1)-1,-1,-1):
# #     if l1[x] in l1[:x]:
# #         l1.pop(x)
# # print(l1)


####joing the items of the list into the one item
# s1=''
# for x in l1:
#     s1+=str(x)
# print((s1))


####identifing the preiority items
# p1=['burger','pizza','chapathi','dosa','rooti']
# p2=['chapathi','rooti','dosa','pizza','burger']
# pre=10
# selected=5
# for i in p1:
#         if i in p2:
#             count=p1.index(i)+p2.index(i)
#             if(count<pre):
#                 pre=count
#                 selected=i
# print(selected)

