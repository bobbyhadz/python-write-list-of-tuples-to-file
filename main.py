# Write a List of Tuples to a File in Python

list_of_tuples = [(1, 'bobby'), (2, 'hadz'), (3, 'com')]

with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(f'{tup[0]} {tup[1]}' for tup in list_of_tuples))