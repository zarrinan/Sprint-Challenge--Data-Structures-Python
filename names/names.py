import time
from bst import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)  # 5.071461915969849 seconds

# Binary search tree would be an optimal data structure to solve this problem
bst = BinarySearchTree(names_1[0])

# Insert names from the names_1 into the bst
for name in names_1[1:]:
    bst.insert(name)

# Check if the bst contains names from the names_2
for name in names_2:
    if bst.contains(name):
        # If there are same names, append to the dublicates
        duplicates.append(name)  # 0.0876319408416748 seconds

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# It would be sets, completed in 0.003823995590209961 seconds, faster than BST
duplicates = set(names_1).intersection(names_2)
