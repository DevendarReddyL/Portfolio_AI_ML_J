fruits =["apple","banana","Mango"]
print(fruits)
print(fruits[0])
print(fruits[-1])

fruits.append("cherry")
fruits.insert(1,"grapes")
print(fruits)
fruits.pop()
print(fruits)
del fruits[0]
print(fruits)
print(fruits[:2])
print(fruits[-2:])

#numbers
numbers=[10,6,8,11,18,20,1,99]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))
print(max(numbers))

#lists using for loop

names=["dev","ashish","karthik","pavan"]
for name in names:
    print(name)