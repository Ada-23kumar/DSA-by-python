# Given a list of heterogeneous elements. Write a python script to remove all the non int values from the list
l1 = [23, 45, "Adae", "ar", "af", 45, "gr"]
new_list = []

for item in l1:
    if isinstance(item, int):
        new_list.append(item)

print("Numbers:", new_list)


l2 = [23, 45, "Adae", "ar", "af", 45, "gr"]

for var in l2:
    if isinstance(var,str):
        l2.remove(var)

print(l2)
