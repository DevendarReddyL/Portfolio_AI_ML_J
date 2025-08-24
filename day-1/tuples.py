
tuple=(5,)
print(tuple)
# Creating a tuple
tuple=(5,"Dev",12.4,True)
print(tuple)
print(type(tuple))
# Accessing elements
print(tuple[0])

#Negative index
print(tuple[-1])

#length of my tuple
print(len(tuple))

#operations in tuples

a=(1,2,3,4)
b=(5,67,7,8)
#concatenation
print(a+b)
#repetition
print(a*2) 
#Membership
print(2 in a)
#iteration
for i in a:
    print(i)
#tuples Methods
d=(1,2,34,5,53,3,3,3,22,2,2)

print("length of d tuple is : ",len(d))
print("count of 2 is ",d.count(2))
print("index of 3 is", d.index(3))