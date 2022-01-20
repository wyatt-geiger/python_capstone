# example of sets, which are similar to lists but do not allow duplicate values
# the check for duplicate values is done internally. no error will be shown when attempting to add a duplicate value,
# it just won't show up in the set

cats = set()

cats.add('Lion')
cats.add('Cheetah')

print('-----')

print(cats)

print('-----')

for animal in cats: # loops over the set, printing each element line by line
    print(animal)

print('-----')

cat_list = ['Lion', 'Cheetah', 'Lion', 'Panther']
# sets are useful when you want to remove duplicates. you can convert a list into a set as shown below

cat_list_no_dupes = list(set(cat_list))

print(cat_list_no_dupes)