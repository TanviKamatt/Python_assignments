#Write a program to count the number of vowels, consonants, digits, and special characters in a given string.
def countchar(userstr):
    vowels="aeiou"
    consonants="bcdfghjklmnpqrstvwxyz"
    digits="0123456789"
    countv=0
    countc=0
    countd=0
    countsp=0

    for i in userstr:
        if i in vowels:
            countv+=1
        elif i in consonants:
            countc+=1
        elif i in digits:
            countd+=1
        elif not i.isspace():
            countsp+=1

    return countv,countc,countd,countsp

userstr=input("Enter a string:")
print("count of vowels,consonants,digits,or special characters:",countchar(userstr))

#ques2
#Given a string, reverse each word individually without changing the word order.
def reversestr(userstr):
    words=userstr.split()

    rev_str=[]
    for i in words:
        rev_str.append(i[::-1])

    return " ".join(rev_str)

userstr=input("Enter a string:")
print("reversed string:",reversestr(userstr))

# Check whether a given string is a palindrome using indexing and slicing.
userstr = input("Enter a string:")
if userstr == userstr[::-1]:
    print(userstr, "is a palindrome")
else:
    print(userstr, "is not a palindrome")


# Write a program to find the frequency of each character in a string.
def frequency(userstr):
    freq = {}
    for char in userstr:
        freq[char] = freq.get(char, 0) + 1
    return freq


userstr = input("Enter a string:")
charfreq = frequency(userstr)
print("character freq:")
for char, count in charfreq.items():
    print(char, ":", count)


#Demonstrate string immutability by attempting to modify a character and handling the error.
userstr = "Hello World"
try:
    userstr[0]="h"

except TypeError as e:
    print("error ",e)
    print("string is immutable:",userstr)

newstr="h"+userstr
print("new str:", newstr)