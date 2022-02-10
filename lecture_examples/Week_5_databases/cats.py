from peewee import *

db = SqliteDatabase('cats.sqlite')

class Owner(Model):
    name = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return f'{self.id}: {self.name}'

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()
    owner = ForeignKeyField(Owner, backref='cats')

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.color}, {self.age}, Owner: {self.owner}'

db.connect()
db.create_tables([Cat, Owner])

Cat.delete().execute() # clear the database table

sam = Owner(name='Sam')
sam.save()
lily = Cat(name='Lily', color='Black', age=1, owner=sam)
lily.save()

print(lily)
print(lily.owner.name)

zoe = Cat(name='Zoe', color='Ginger', age=3)
zoe.save() # make sure to save or else it won't be saved to the database

holly = Cat(name='Holly', color='Tabby', age=5)
holly.save()

fluffy = Cat(name='Fluffy', color='Black', age=1)
fluffy.save() # create

for cat in Cat.select(): # read
    print(cat)

list_of_cats = list(Cat.select()) # converts query object to Python list

""" CRUD operations
Create - insert
Read - select
Update
Delete
"""

fluffy.age = 2 # update
fluffy.save()

print('After Fluffy\'s age changed')
for cat in Cat.select():
    print(cat)

# can update many rows if needed
rows_modified = Cat.update(age=6).where(Cat.name == 'Holly').execute()

print('After Holly\'s age changed')
for cat in Cat.select():
    print(cat)

print(rows_modified) # prints number of rows updated; in this case just 1 row was updated

buzz = Cat(name='Buzz', color='Gray', age=3)
buzz.save()

cats_who_are_3 = Cat.select().where(Cat.age == 3)
for cat in cats_who_are_3:
    print(cat, ' is three')

cat_with_l_in_name = Cat.select().where(Cat.name % '*b*') # this is case sensitive
                                        # case insensitive: Cat.name.contains('b')
for cat in cat_with_l_in_name:
    print(cat, 'has l in name')

zoe_from_db = Cat.get_or_none(name='Zoe')
print(zoe_from_db)

cat_1 = Cat.get_by_id(1) # can also use Cat.id == 1 to find the entry at that position
print(cat_1)

rows_delete = Cat.delete().where(Cat.name == 'Holly').execute() # delete
print(rows_delete, list(Cat.select()))

# Count, sort, limit
total = Cat.select().count()
print(total)

total_cats_who_are_5 = Cat.select().where(Cat.age == 5).count()
print(total_cats_who_are_5)

cats_by_name = Cat.select().order_by(Cat.name) # could also order by something like age
print(list(cats_by_name))

cats_by_name = Cat.select().order_by(Cat.name.desc()) # same as above but list is reversed
print(list(cats_by_name))

first_3 = Cat.select().order_by(Cat.name).limit(2)
print(list(first_3))