#Write a program to insert 5 states in a set1 and 5 states in another set display states present inboth sets, display states in set1 but not in set2 and display all states in both sets. Update a
#dictionary with the total number of vowels found in each item in the set. Where the key willbe the state.

set1 = set()
set2 = set()
set3 = set()
set4 = set()
set5 = set()
set1 = {"kerala","tamilnadu","karnataka","andhra pradesh","telangana"}
set2 = {"delhi","punjab","haryana","uttar pradesh","bihar","kerala","tamilnadu"}
set3 = set1.intersection(set2)
set4 = set1.difference(set2)
set5 = set1.union(set2)
print("States present in both sets:",set3)
print("States present in set1 but not in set2:",set4)
print("All states in both sets:",set5)
set6 = dict()
for i in set1:
    for j in i:
        if j in 'aeiou':
            set6[i.count(j)]=j
print(set6)
            


