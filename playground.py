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
	db = c.execute('''
		SELECT * 
		FROM stocks
	''')
	print '\n************************************'
	for row in db:
		print row
	print '************************************\n'

def update_pay_by_first_name(conn):
	c = conn.cursor()
	update_list = [
		('John', 'Doe', 120, 20),
		('Alice', 'Anderson', 95, 20),
		('Bob', 'Brown', 85, 30)
	]
	c.execute('''
		INSERT INTO stocks (firstname, lastname, salary, bonus)
		VALUES
			('John', 'Doe', '120', '20'),
			('Alice', 'Anderson', '95', '20'),
			('Bob', 'Brown', '85', '30')
		ON DUPLICATE KEY UPDATE
			salary=VALUES(salary), bonus=VALUES(bonus)
	''')
	conn.commit()



if __name__ == '__main__':
	conn = create_connection('example.db')
	experiment(conn)
	close_connection(conn)

























