# Create a list with your friends' names.
names = ['kyle', 'jeanette', 'jaylynn', 'cathy']

# Print each name with a capital.
print(names[-1].title())
print(names[-2].title())
print(names[0].title())
print(names[1].title())

# Print the same message to each friend on the list.
print("\n")
print("Hello,", names[0].title() + "!")
print("Hello,", names[1].title() + "!")
print("Hello,", names[2].title() + "!")
print("Hello,", names[3].title() + "!")

# Print each name using fewer print lines and teired tabs.
print("\n")
print(names[2].title(), "\n\t" + names[1].title())
print("\t\t" + names[0].title(), "\n" + "\t"*3 + names[3].title())
