for i in range (1,10):
    if i ==5:
        print("Breaking at i :",i)
        break
    print(i)

for i in range (1,10):
    if i==5:
        print("skipping at i:",i)
        continue
    print(i)
 

for i in range (1,10):

    if i==5:
        print("Skipping at i :",i)
        continue
    if i==8:
        print("breaking at i:",i )
        break
    print(i)