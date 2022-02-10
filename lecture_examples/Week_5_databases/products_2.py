import sqlite3

# validation errors, rowid
# rowid is used as an auto-incrementing primary key
    # this is created only if there are no other INT columns that are UNIQUE

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT UNIQUE, quantity INT)')
    
    # you can also specify the primary key with code above
    # when doing this, you MUST specify the names in insert, update, delete statements (line 24 below)
    
    # OLD CODE: conn.execute('CREATE TABLE IF NOT EXISTS products (name TEXT UNIQUE, quantity INT)')

conn.close()

name = 'gloves'
quantity = 5

try: # without try/except, program crashes with IntegrityError
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))
                                        # name, quantity must be specified here
                                        # when explicitly declaring product_id as PRIMARY KEY
    conn.close()
except Exception as e:
    print('Error inserting', e)

conn = sqlite3.connect(db)
results = conn.execute('SELECT rowid, * FROM products')
for row in results:
    print(row)

print('End of program!')