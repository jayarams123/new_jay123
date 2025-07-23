str1 = "my name is jayaram"
str2 = "nice to meet you"
str3 = 'aeiou'
count =0
common = ''
joined = ''
joined1 =''
for i in str1:
    for j in str2:
        if i==j:
            common += i


joined = set(common)
for ch in joined:
    if ch != ' ':
        joined1 += ch
print(f"joined {joined}  joined1:{joined1} ")

for c in joined:
    if c in str3:
        count += 1
print(joined1)
print(count)

