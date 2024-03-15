# Practice with lists.
groceries = ['apples', 'pears', 'milk']
print(groceries)

# Add item to end of list.
groceries.append('bread')
groceries.append('eggs')
print(groceries)

# Insert item in second position.
groceries.insert(1, 'peppers')
groceries.insert(2, 'squash')
print(groceries)

# Remove an item using the del statement.
del groceries[0]
print(groceries)

# Remove an item using pop.
removedGroceries = groceries.pop()
print(groceries)
print(removedGroceries)

groceries.sort(reverse=True)
print("\n", groceries)

# Sort the list alphabetically.
groceries.sort()
print("\n", groceries)

# Reverse sort the list.
groceries.reverse()
print("\n", groceries)
