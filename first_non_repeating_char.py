from scipy.sparse.linalg import spsolve_triangular

str = "jayaramj"
#loop through str , get first element, compare it with rest of the str to check if first element is in str, if not print it else second element check

# mid = int(len(str)/2)
# str1 = ''
# for i in range(len(str)):
#     j = i + 1
#     for j in range(len(str1)):
#         if (str[i] == str1):
#             print(f" {str[i]} is a Repeating char")
#         else:
#             str1 += str[i]
#             print(f"{str1} is a non repeating first char")
# count = int
# for ch in str:
#     count = 0
#     if ch in str:
#         count += 1
#
# if count == 1:
#     print(f"{ch} is first non-repeating char")

str1 = ''
for ch in str:
    count = 0
    if ch not in str1:
        for ch1 in str:
            if  ch ==  ch1:
                count += 1



        str1 +=  ch
        print(f"{ch} occurs for {count} times ")




