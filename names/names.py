"""
 What is the runtime complexity of this code?
 Initially, with the nested for loops the complexity was O(n^2)
 """
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# Let's use the BST here to load in one list
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare value to see if child should be left or right
        # Check if that child already exists, if so compare it by 
        # running that function again.
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False
duplicates = []  # Return the list of duplicates in this data structure
bst = BSTNode("N")
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     bst.insert(name_1)

# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# First instinct is to try the set
duplicates1 = []
set_1 = set(names_1)
set_2 = set(names_2)
for name_2 in set_2:
    if name_2 in set_1:
        duplicates1.append(name_2)

end_time = time.time()
print (f"{len(duplicates1)} duplicates1:\n\n{', '.join(duplicates1)}\n\n")
print (f"STRETCH runtime: {end_time - start_time} seconds")
print("Why, yes, it does seem to be significantly faster!")