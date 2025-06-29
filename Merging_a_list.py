list1 = [[1,4,5],[1,3,4],[2,6]]
new_list1 = []
for i in list1:
    for j in i:
        new_list1.append(j)

new_list1.sort()
print(new_list1)
