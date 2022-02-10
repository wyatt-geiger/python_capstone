import sqlite3

db = 'improved_first_db.sqlite'

def create_table():
# when using a context manager, you do not need to use conn.commit() as it is done automatically
# if there is any error within the code, the context manager will not finish and will rollback any changes made
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')
    conn.close() # close at end of function

def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products values (1000, "hat")')
        conn.execute('INSERT INTO products values (1001, "jacket")')

    conn.close()

def display_all_data(): # does not require a context manager because you are not committing any changes
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products')
    print('All products: ')
    for row in results:
        print(row) # each row is a tuple

    conn.close()

def display_one_product(product_name):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
    first_row = results.fetchone()
    if first_row:
        print('Your product is: ', first_row) # upgrade to row factory later?
    else:
        print('Not found')

    conn.close()

def create_new_product():

    new_id = int(input('Enter a new ID: ')) # asks for user input to enter a new ID and product name
    new_name = input('Enter a new product name: ')

    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name))
    # you cannot use {new_id} or {new_name} here
    # you MUST use wildcards ? followed by the variables after a comma, because data is stored as a tuple
    
    conn.close()

def update_product():

    update_product = 'wool hat' # update product name hat with wool hat, using the ID to locate product name hat
    update_id = '1000'

    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE products SET name = ? WHERE id = ?', (update_product, update_id))
    
    conn.close()
   
def delete_product(product_name):

    with sqlite3.connect(db) as conn:
        conn.execute('DELETE FROM products WHERE name = ?', (product_name, )) # if you are only using 1 parameter, you still must include a comma after it
    
    conn.close()

create_table()
insert_example_data()
display_all_data()
display_one_product('jacket')
display_one_product('coat')
create_new_product()
update_product()
delete_product('jacket')
display_all_data()