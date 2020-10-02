
Mylist=[1,2,3,4,5,6,7,8,9,10]
Mylist2=["a","b","c","d","e","f","g","h","i","j"]

counter=0

for number in Mylist:
    if number < len(Mylist) -1:
        counter += Mylist[number+1]-Mylist[number]

print(counter)

for x in Mylist:
    print(type(x))
