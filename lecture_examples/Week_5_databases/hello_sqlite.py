import sqlite3

conn = sqlite3.connect('first_db.sqlite') # connect to a database, or create it if doesn't exist

conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')

conn.execute('INSERT INTO products values (1000, "hat")')

conn.execute('INSERT INTO products values (1001, "jacket")')

conn.commit() # use this code after EVERY change or database will not update

results = conn.execute('SELECT * FROM products')

for row in results:
    print(row) # each row is a tuple

results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
first_row = results.fetchone()
print(first_row)

new_id = int(input('Enter a new ID: ')) # asks for user input to enter a new ID and product name
new_name = input('Enter a new product name: ')

conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name))
# you cannot use {new_id} or {new_name} here
# you MUST use wildcards ? followed by the variables after a comma, because data is stored as a tuple
conn.commit()

update_product = 'wool hat' # update product name hat with wool hat, using the ID to locate product name hat
update_id = '1000'
conn.execute('UPDATE products SET name = ? WHERE id = ?', (update_product, update_id))
conn.commit()

delete_product = 'jacket' # deletes product name jacket from database
conn.execute('DELETE FROM products WHERE name = ?', (delete_product, )) # if you are only using 1 parameter, you still must include a comma after it
conn.commit()

conn.close()