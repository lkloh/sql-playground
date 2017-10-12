import sqlite3



def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
    	conn = sqlite3.connect(db_file)
    	c = conn.cursor()
    	c.execute('''
    		CREATE TABLE IF NOT EXISTS stocks 
    		(
    			firstname text,
    			lastname text,
    			salary int,
    			bonus int,
    			PRIMARY KEY(firstname, lastname)
    		)''')
    	return conn
    except:
    	raise

def close_connection(conn):
    conn.close()



def experiment(conn):
	insert_row(conn)
	update_pay_by_first_name(conn)

def insert_row(conn):
	c = conn.cursor()
	c.execute('''INSERT INTO stocks VALUES ('John', 'Doe', 100, 15)''')
	c.execute('''INSERT INTO stocks VALUES ('Jane', 'Roe', 110, 5)''')
	c.execute('''INSERT INTO stocks VALUES ('Alice', 'Anderson', 80, 20)''')
	c.execute('''INSERT INTO stocks VALUES ('Bob', 'Brown', 70, 30)''')
	conn.commit()
	print_db(conn)

def print_db(conn):
	c = conn.cursor()
	db = c.execute('''SELECT * FROM stocks''')
	print '\n\n************************************'
	for row in db:
		print row
	print '************************************\n\n'

def update_pay_by_first_name(conn):
	c = conn.cursor()
	update_list = [
		('John', 'Doe', 120, 20),
		('Alice', 'Anderson', 95, 20),
		('Bob', 'Brown', 85, 30)
	]

	# check that the primary key is present first
	entry_in_db = c.execute('''
		SELECT count(*) 
		FROM stocks 
		WHERE firstname = 'John' AND lastname = 'Doe'
	''')
	result = c.fetchall()
	if result[0][0] == 1:
		c.executescript('''
			UPDATE stocks
			SET salary = 120, bonus = 20
			WHERE firstname = 'John' AND lastname = 'Doe'
		''')
		conn.commit()

	print_db(conn)


if __name__ == '__main__':
	conn = create_connection('example.db')
	experiment(conn)
	close_connection(conn)



















