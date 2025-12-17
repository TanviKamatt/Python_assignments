#Write a program to remove duplicate elements from a list without using set.
def duplicate(userlist):
    newlist = []
    for item in userlist:
        if item not in newlist:
            newlist.append(item)

    return newlist
userlist=[1,2,3,4,5,2,3,4,5,6,1]
newlist=duplicate(userlist)
print("original list:",userlist)
print("new list:",newlist)

#ques2
def evennums(num):
    even=[]
    for n in num:
        if n%2==0:
            even.append(n)
    return even

num=[1,2,3,4,5,22,33,44,66,88]
print("original list:",num)
print("even nums list:",evennums(num))

#ques3
#Write a program to find the second largest element in a list.
def secondlargest(nums):
    numbers=sorted(list(set(nums)), reverse=True)
    if len(numbers)<2:
        return "list must have atleast 2 elements"
    else:
        return numbers[1]

nums=[1,2,3,10,20]
print("original list:",nums)
print("second largest:",secondlargest(nums))

#ques4
def suminner(nums):
    sums=[]
    for innerlist in nums:
        cursum=sum(innerlist)
        sums.append(cursum)
    return sums

nums=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("original list:",nums)
print("sum:",suminner(nums))

#ques5
import copy

original_list=[1,2,['a','b']]

sh_cpy=copy.copy(original_list)
deep_copied=copy.deepcopy(original_list)

print("original list:",original_list)
print("deep copied list:",deep_copied)
print("shallow copied list:",sh_cpy)

original_list[2].append('x')
original_list.append(3)
print("original list:",original_list)
print("deep copied list:",deep_copied)
print("shallow copied list:",sh_cpy)