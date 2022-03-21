# str = 'abebba'

# isPelindrom =True

# # for i in range(0,(len(str)//2+1)):
# #     if str[i]!=str[len(str)-i-1]:
# #         isPelindrom=False


# # print(isPelindrom)


# def checkPelindrom(str,i,j):
#     if(i>j):
#         return
#     if(str[i]!=str[j]):
#         global isPelindrom
#         isPelindrom=False
#         return
#     return checkPelindrom(str,i+1,j-1)

# checkPelindrom(str,0,len(str)-1)

# print(isPelindrom)



# sum=0
# num=1234

# while num>0:
#     sum +=(num%10)
#     num=num//10

# print(sum)


def fun(num,n1,n2,n3):
    if num<0:
        return -1
    if num==0:
        return 0
    l1=fun(num-11,11,9,12)
    l2=fun(num-9,11,9,12)
    l3=fun(num-12,11,9,12)
    maxValue =max(l1,l2,l3)
    if maxValue >= 0:
        maxValue+=1
        return maxValue
    return -1
    


print(fun(23,11,9,12))
