set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

unionset = set1 | set2

print(f"Union: ",unionset)

intersectionset = set1 & set2

print(f"Intersection: ",intersectionset)

differenceset = set1 - set2
print(f"Difference (set1 - set2): ",differenceset)

symmetricset = set1 ^ set2
print(f"Symmetric Difference: ",symmetricset)

#ques 2

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

setunique = set_a - set_b
allelements = set_a ^ set_b

print(f"Set A after removing common elements: ",setunique)
print(f"All unique elements from both sets: ",allelements)

#ques3
parent = {1, 2, 3, 4, 5, 6}
child = {2, 4, 6}
newset = {1, 7}

is_subset1 = child <= parent

print(child," is a subset of", parent,":" ,is_subset1)

is_subset2 = newset <= parent
print(newset," is a subset of ", parent," : ",is_subset2)

#ques4
number_set = {10, 4, 20, 15, 3, 25}
thresh = 12

print("Elements greater than ",thresh, ":")
for number in number_set:
    if number > thresh:
        print(number)

#ques5
dup_list = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

unique_set = set(dup_list)
print("Unique set: ",unique_set)

unique_list = list(unique_set)
print("List with unique elements:",unique_list)