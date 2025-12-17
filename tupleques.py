#ques1
def max_min(tup):
    if not tup:
        return None,None

    maxel=tup[0]
    minel=tup[0]

    for i in tup[1:]:
        if i>maxel:
            maxel=i
        if i<minel:
            minel=i

    return maxel,minel

tup=(1,2,3,5,7,9)
print("original tuple:",tup)
print("maximum and minimum elements:",max_min(tup))

#ques2
def tuple_to_dict(tup):
    newdict={}
    for key,value in tup:
        newdict[key]=value
    return newdict

list_of_tups=[(1,2),(3,4),(5,6),(7,8)]
print("original list:",list_of_tups)
print("result:", tuple_to_dict(list_of_tups))

#ques3
def count_element(tup,element):
    count=0
    for i in tup:
        if i==element:
            count +=1
    return count

tup=(1,2,3,4,1,2,1,5,6)
element=1
print("original list:",tup)
print("count of element",element,":",count_element(tup,element))

#ques4
tup=(1,[2,3],4)
print("original list:",tup)
print("before modification of inside list:",tup)
tup[1].append(5)
tup[1][0]=10
print("after modification of inside list:",tup[1])
print("tuple after modification:",tup)

#ques5
tup1 = (1, 2, 3)
tup2 = ('a', 'b', 'c')

print(f"Before swap:")
print(f"Tuple 1: {tup1}")
print(f"Tuple 2: {tup2}")

tup1, tup2 = tup2, tup1

print(f"After swap:")
print(f"Tuple 1: {tup1}")
print(f"Tuple 2: {tup2}")