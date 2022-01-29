

# def max_count(n, a, b, c):
#     if n < 0:
#         return -1
#     if n == 0:
#         return 0
#     max_value = max(max_count(n-a, a, b, c),
#                     max_count(n-b, a, b, c),
#                     max_count(n-c, a, b, c))
#     if max_value >= 0:
#         max_value += 1
#         return max_value
#     return -1


# print(max_count(11, 2, 2, 11))


# def print_string(str, org_str, added_str, i):

#     if i == len(str)-1:
#         print("{}+{}".format(org_str, org_str+added_str))
#         # print(org_str+added_str)
#         return
#     i+=1
#     print_string(str, org_str, str[i], i)
#     print_string(str, org_str+added_str, str[i], i)
#     return


# print_string("ABCD", "", "A", 0)




