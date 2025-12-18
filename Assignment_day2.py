# Write a function that takes a list of integers and returns a new list containing only the even numbers.
def filter_even(num):
    evennum=[]
    for i in num:
        if i%2==0:
            evennum.append(i)
    return evennum

num=[1,2,3,4,5,6]
print("original list:",num)
print("filtered list:",filter_even(num))

#Write a function that accepts a string and returns a dictionary with the count of each character in the string.

def count_char(inp):
    count={}
    for i in inp:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
inp="hello hello"
print("original input:",inp)
print("character count:",count_char(inp))


#Write a function that takes a number as input and returns True if it is a palindrome, otherwise False.

def is_palindrome(num):
    newnum=str(num)
    return newnum==newnum[::-1]

num=int(input("Enter a number:"))
print("is ",num," a palindrome?",is_palindrome(num))

#Write a function that accepts variable-length arguments (*args) and returns the average of the numbers.

def calc_avg(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print("Avg of 1,2,3,4,5 is:",calc_avg(1,2,3,4,5))

#Write a function that takes two lists and returns a list of common elements without using built-in set operations.
def find_common(l1,l2):
    common=[]
    for i in l1:
        if i in l2 and i not in common:
            common.append(i)
    return common

l1=[1,2,3,4,5,9]
l2=[6,7,2,3,9,1]
print("list 1:",l1)
print("list 2:",l2)
print("Common elements:",find_common(l1,l2))
