num=[1,2,3,4,5,6,7]
first=0
last=len(num)-1
middle=(first+last)//2
num[2]
print(num[middle])
# printing element at index five to eleven
num[5]=11
print(num)
num[2]='student'
num[1]='mother'
print(num)
# looping through indexes
for x in range(len(num)):
    print(x)
# looping through elements
for x in num:
    print(x)

