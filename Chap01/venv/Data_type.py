str = [1,2,'a','abc',(11,12)]
str2 = [(8,9)]
val = 1 not in str

print(val)

str.append('s')
print(str)
last_elem = str.pop()
print(last_elem)

str.extend((5,6))
print(str)
str.extend(str2)
print(min(str))