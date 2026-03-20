string1=input("enter the 1st word")
string2=input("enter the 2nd word")
if(len(string1)==len(string2)):
    for a in string1:
        print("no"if a not in string2 else "yes")
    # for a in string1:
    #     if a not in string2:
    #         print("no it is not anagram")
    #         break
    #     else:
    #         print("yes it is angram")
    #         break

